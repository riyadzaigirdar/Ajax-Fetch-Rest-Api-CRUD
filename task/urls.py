from django.urls import path
from . import views

urlpatterns = [
	path('', views.api_root),
	path('list/', views.tasklist.as_view()),
	path('detail/<int:pk>/', views.taskdetail),
	path('create/', views.taskcreate),
	path('update/<int:pk>/', views.taskupdate),
	path('delete/<int:pk>/', views.taskdelete),
]
