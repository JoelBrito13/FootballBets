from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BetView.as_view(),
        name='bets'
    ),
]
