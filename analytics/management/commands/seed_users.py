from django.core.management.base import BaseCommand
from analytics.models import UserActivity
import random

class Command(BaseCommand):
    help = "Seed database with dummy user activity data"

    def handle(self, *args, **kwargs):
        UserActivity.objects.all().delete()

        users = []
        for i in range(1, 501):
            users.append(
                UserActivity(
                    user_id=i,
                    login_count=random.randint(1, 100),
                    avg_session_time=round(random.uniform(1, 60), 2),
                    days_inactive=random.randint(0, 30),
                    feature_usage=random.randint(1, 50),
                    churned=random.choice([True, False])
                )
            )

        UserActivity.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS("✅ 500 users inserted successfully"))
