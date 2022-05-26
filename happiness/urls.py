from django.urls import path

from . import views

app_name = 'happiness'
urlpatterns = [
    # path('', views.index, name='index'),
    path('create/', views.CreateHappiness.as_view(), name = "happiness_form"),
    path('list/', views.ListHappinessView.as_view(), name = "happiness_list"),
]
