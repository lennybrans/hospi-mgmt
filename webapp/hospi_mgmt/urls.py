from django.urls import path
from django.contrib.auth.decorators import login_required

from hospi_mgmt import views as vw

urlpatterns = [
    path('', vw.index, name='index'),
    path('home', vw.home, name='home'),
    path('gato', vw.gato_view, name='gato'),
    path('perro', vw.perro_view, name='perro'),
    path(
        '<int:pk>/create',
        login_required(vw.OccupantCreate.as_view()),
        name='create'
    ),
    path(
        '<int:pk>/edit',
        login_required(vw.OccupantUpdate.as_view()),
        name='edit'
    ),
    path(
        '<int:pk>/detail',
        login_required(vw.OccupantDetail.as_view()),
        name='detail'
    ),
    path(
        '<int:pk>/delete',
        login_required(vw.OccupantDelete.as_view()),
        name='delete'
    ),
]
