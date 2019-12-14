from django.conf.urls import url

from users import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.get_users,
        name='users'
    ),
    url(
        regex=r'^login/$',
        view=views.ObtainAuthToken.as_view(),
        name='login'
    ),
    url(
        regex=r'^balance/$',
        view=views.Balance.as_view(),
        name='balance'
    ),
    url(
        regex=r'^balance/(?P<amount>[0-9]+)$',
        view=views.Balance.as_view()
    ),
]
