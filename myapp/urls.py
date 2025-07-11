
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('',views.register, name='register'),
    path('login/',views.login_view, name='login'),
]
