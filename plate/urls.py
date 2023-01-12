from django.urls import path
from . import views
urlpatterns = [
    path('generate/',views.GeneratePlateView.as_view()),
    path('get/',views.GetPlateView.as_view()),
    path('add/',views.AddPlateView.as_view()),

]
