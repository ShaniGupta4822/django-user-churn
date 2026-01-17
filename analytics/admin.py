from django.contrib import admin
from .models import UserActivity

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'login_count',
        'avg_session_time',
        'days_inactive',
        'feature_usage',
        'churned',
        'created_at',
    )
