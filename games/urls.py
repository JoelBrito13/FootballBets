from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^register/$',
        view=views.RegisterView.as_view(),
        name='register'
    ),

    url(
        regex=r'^login/$',
        view=views.LoginView.as_view(),
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    url(
        regex=r'^members/$',
        view=views.MembersView.as_view(),
        name='members'
    ),
    url(
        regex=r'^search/$',
        view=views.SearchGame.as_view(),
        name='search game'
    )
]
