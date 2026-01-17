import os
import sys

# 🔑 Project root path add karo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import pandas as pd
from analytics.models import UserActivity
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1️⃣ DB se data uthao
qs = UserActivity.objects.all().values()
df = pd.DataFrame(qs)

# 2️⃣ Features & target
X = df[['login_count', 'avg_session_time', 'days_inactive', 'feature_usage']]
y = df['churned']

# 3️⃣ ML model train karo
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 4️⃣ Model save karo
with open(os.path.join(BASE_DIR, 'ml', 'churn_model.pkl'), 'wb') as f:
    pickle.dump(model, f)

print("✅Model trained successfully using SQL (Django ORM)")
