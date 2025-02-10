from django.urls import path
from . import views

urlpatterns = [
    path('http/', views.http_response_view, name='http_response'),
    path('render/', views.render_view, name='render_view'),
]