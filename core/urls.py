
from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register_view,name='registerview'),
    path('login/',views.login_view,name='loginview'),
    path('logout/',views.register_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard')
]
