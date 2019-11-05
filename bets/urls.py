from django.conf.urls import  url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BetView.as_view(),
        name='bets'
    ),
    url(
        regex=r'^alter/(?P<bet>\d{4})/$',
        view=views.Alter.as_view(),
        name='alter'
    ),
    url(
        regex=r'^test/$',
        view=views.Test.as_view(),
        name='test'
    ),
]
