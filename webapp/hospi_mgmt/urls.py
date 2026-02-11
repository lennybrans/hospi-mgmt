from django.urls import path

from hospi_mgmt import views as vw

urlpatterns = [
    path('', vw.index, name='home'),
    path('gato', vw.gato_view, name='gato'),
    path('perro', vw.perro_view, name='perro'),
    path('<int:pk>/create', vw.OccupantCreate.as_view(), name='create'),
    path('<int:pk>/edit', vw.OccupantUpdate.as_view(), name='edit'),
    path('<int:pk>/detail', vw.OccupantDetail.as_view(), name='detail'),
    path('<int:pk>/delete', vw.OccupantDelete.as_view(), name='delete'),
]
