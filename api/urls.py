from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('seccion/<int:seccion_id>', views.SeccionView.as_view(), name='id-seccion'),
    path('seccion/', views.SeccionView.as_view(), name='all-seccion'),
    path('elemento/<int:elemento_id>', views.ElementoView.as_view(), name='id-elementos'),
    path('elemento/', views.ElementoView.as_view(), name='all-elementos'),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('register', views.Register.as_view(), name="register"),
]