from django.urls import path
from task.views import manager_dashboard,user_dashboard

urlpatterns = [
    path("manager_dashboard/",manager_dashboard),
    path("user_dashboard/",user_dashboard),
]
