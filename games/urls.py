from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search game'
    )
]
