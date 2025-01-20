from django.urls import path
from . import views

urlpatterns = [
    path('',views.callTemplateSelectorPage,name='template')
]