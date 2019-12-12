from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BetView.as_view(),
        name='bets'
    ),
    url(
        regex=r'^game/(?P<match_id>[0-9]+)/$',
        view=views.view_game,
        name='game'
    ),

]
