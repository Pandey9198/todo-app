from django.urls import path
from .views import (
    task_list, set_in_progress, set_pending, mark_done, view_task, delete_task,
    user_register, user_login, user_logout,
    CustomPasswordResetView, CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
)

urlpatterns = [
    path("", task_list, name="task_list"),
    path("in-progress/<int:task_id>/", set_in_progress, name="set_in_progress"),
    path("pending/<int:task_id>/", set_pending, name="set_pending"),
    path("done/<int:task_id>/", mark_done, name="mark_done"),
    path("task/<int:task_id>/", view_task, name="view_task"),
    path("delete/<int:task_id>/", delete_task, name="delete_task"),
    
    # Authentication URLs
    path("register/", user_register, name="user_register"),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    
    # Password Reset URLs
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/confirm/<uidb64>/<token>/", CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
