
from django.contrib import admin
from django.urls import path,include
from task.views import Home,Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",Home),
    path("task/",include("task.urls"))
]
