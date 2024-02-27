from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.HomePost.as_view(),name='home'),

]