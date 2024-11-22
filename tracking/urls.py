from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.aboutpage, name="aboutpage"),
    path('contact/', views.contactpage, name="contactpage"),
    path('track/', views.tracking_page, name='tracking'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
]

urlpatterns += staticfiles_urlpatterns()
