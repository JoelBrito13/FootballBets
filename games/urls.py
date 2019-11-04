from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^search/$',
        view=views.SearchView.as_view(),
        name='search game'
    ),
    url(
        regex=r'$',
        view=views.GameView.as_view(),
        name='games'
    )
]
