import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import pandas as pd
from analytics.models import UserActivity
from sklearn.ensemble import RandomForestClassifier
import pickle

qs = UserActivity.objects.all().values()
df = pd.DataFrame(qs)

X = df[['login_count', 'avg_session_time', 'days_inactive', 'feature_usage']]
y = df['churned']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

with open(os.path.join(BASE_DIR, 'ml', 'churn_model.pkl'), 'wb') as f:
    pickle.dump(model, f)

print("✅Model trained successfully using SQL (Django ORM)")
