
from django.urls import path

from task.views import manager_dashboard,user_dashboard,create_task,view_task

urlpatterns = [
    path("manager_dashboard/",manager_dashboard),
    path("user_dashboard/",user_dashboard),
    path("create_task/",create_task),
    path("view_task/",view_task)
]
