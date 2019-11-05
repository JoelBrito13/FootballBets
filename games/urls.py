from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'$',
        view=views.GameView.as_view(),
        name='games'
    )
]
