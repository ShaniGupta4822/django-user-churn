import os
import sys
import random
import django

# Django setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from analytics.models import UserActivity

def generate_users(n=500):
    UserActivity.objects.all().delete()  # purana data clear (optional)

    for i in range(1, n + 1):
        login_count = random.randint(1, 60)
        avg_session_time = random.uniform(2, 200)
        days_inactive = random.randint(0, 30)
        feature_usage = random.randint(1, 25)

        # realistic churn logic
        churn_probability = (
            0.4 * (days_inactive / 30) +
            0.3 * (1 - login_count / 60) +
            0.3 * (1 - feature_usage / 25)
        )

        churned = churn_probability > 0.5

        UserActivity.objects.create(
            user_id=i,
            login_count=login_count,
            avg_session_time=avg_session_time,
            days_inactive=days_inactive,
            feature_usage=feature_usage,
            churned=churned
        )

    print(f"✅ {n} users generated successfully")

if __name__ == "__main__":
    generate_users(500)
