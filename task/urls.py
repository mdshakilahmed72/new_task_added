from django.urls import path
from task.views import Contact

urlpatterns = [
    path("contact/",Contact),
]
