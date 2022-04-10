from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_gms, name='index'),
    path('view/<str:type>/<int:id>', views.view, name='index'),
    path('view_gms/', views.view_gms, name='index'),
    path('view_rgms/', views.view_rgms, name='index'),
    path('view_agms/', views.view_agms, name='index'),
    path('view_dms/', views.view_dms, name='index'),
    path('form/<str:type>/<int:id>', views.form, name='form'),
    path('add/<str:type>/<int:id>', views.add_sales, name='form'),
    path('rm/<str:type>/<int:id>', views.remove_sales, name='form'),
    path('submit/<str:type>/<int:fk>', views.submit, name='submit')
]
