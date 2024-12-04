from django.urls import path
from . import views
urlpatterns = [
    path('gettodos/',views.TodoGetView.as_view()),
    path('<str:id>/',views.TodoDetailView.as_view()),
]