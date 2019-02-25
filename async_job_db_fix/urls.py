from django.contrib import admin
from django.urls import path
from core.views import TasksHomeFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TasksHomeFormView.as_view(), name='home'),
]
