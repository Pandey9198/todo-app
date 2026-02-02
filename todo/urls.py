from django.urls import path
from .views import task_list, mark_done, view_task, delete_task

urlpatterns = [
    path("", task_list, name="task_list"),
    path("done/<int:task_id>/", mark_done, name="mark_done"),
    path("task/<int:task_id>/", view_task, name="view_task"),
    path("delete/<int:task_id>/", delete_task, name="delete_task"),
]
