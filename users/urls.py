from django.conf.urls import url

from users import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.get_users,
        name='users'
    ),
]
