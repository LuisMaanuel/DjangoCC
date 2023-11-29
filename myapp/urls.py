from django.urls import path
from . import views
urlpatterns =[
    path('',views.index),
    path('hello/',views.hello),
    path('projects/',views.projects),
    path('create/',views.create_task),
    path('eliminar/<int:id_comp>/',views.delete,name='delete'),
    # path('edicion/<int:id_comp>/', views.pestaña_editar, name='pestaña_editar'),

    path('editar/<int:id_comp>/',views.editar,name='editar'),
]