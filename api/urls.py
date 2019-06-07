from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
]