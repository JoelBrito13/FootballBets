from django.forms import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from games.forms import SearchGame


class SearchGame(forms.Form, TemplateView, View):
    template_name = 'game_template.html'

    def search_game(self, request):
        if request.method == 'POST':
            form = SearchGame(request.POST)
            if form.is_valid():
                query = form.cleaned_data['query']
                games = SearchGame.objects.filter(title_itenscontains=query)
                return render(request, 'game_template.html', {'Games': games, 'Query: ':query})
        else:
            form = SearchGame()
        return render(request, 'game_template.html', {'Form': form})

    def get(self, request, *args, **kwargs):
        self.search_game(request)
        return super(SearchGame, self).get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(SearchGame, self).get_context_data(**kwargs)
    #     context['print_data'] = self.print_data()
    #     return context
