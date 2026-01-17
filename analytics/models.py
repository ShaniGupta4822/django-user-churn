from django.db import models

class UserActivity(models.Model):
    user_id = models.IntegerField()
    login_count = models.IntegerField()
    avg_session_time = models.FloatField()   
    days_inactive = models.IntegerField()
    feature_usage = models.IntegerField()
    churned = models.BooleanField()  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id}"
