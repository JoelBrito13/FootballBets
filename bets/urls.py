from django.conf.urls import  url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BetView.as_view(),
        name='bets'
    ),
    url(
        regex=r'^register/$',
        view=views.Register.as_view(),
        name='alter'
    ),
]
