from django.urls import path, include
from .import views

urlpatterns = [
    # path('',views.chaihome, name="chaihome"),
    path('',views.todolist, name="todo_list"),
    path('add_todo/',views.todo_add,name='todo_add'),
    path('<int:todo_id>/edit/', views.todoedit, name="edit_todo"),
    path('<int:todo_id>/delete/', views.deletetodo, name="delete_todo"),
    path('registration/',views.registration, name="registration"),
    path('search/', views.search, name='search'),

    
    path('__reload__/', include('django_browser_reload.urls')),
] 
