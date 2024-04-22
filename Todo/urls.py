from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',views.markdone,name='mark_as_done'),
    path('mark_undo/<int:pk>/',views.markundo,name='mark_undo'),
    path('editTask/<int:pk>/',views.editTask,name="editTask"),
    path('deleteTask/<int:pk>/',views.deleteTask,name='deleteTask'),
    
    
    
]
