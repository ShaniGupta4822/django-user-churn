# 🚀 Django User Churn Prediction System

This project was built as a hands-on learning exercise to understand how
Machine Learning models can be integrated into a Django web application
for real-world business problems like user churn.


## 📌 Features

- 🔐 Django Admin Panel for managing user activity data
- 📊 Interactive User Churn Dashboard
- 🤖 Churn prediction using a Random Forest model trained on synthetic user behavior data
- 📈 Churn probability & risk level calculation
- 🗄️ MySQL database integration
- 🧪 Synthetic data generation for testing (500+ users)
- 🔎 Search users by User ID

---

## 🛠️ Tech Stack

### Backend
- Python 3
- Django 3.2
- Django ORM
- MySQL

## 💡 Design Decisions

- **Django** was chosen for its built-in admin panel and rapid backend development.
- **MySQL** was used instead of SQLite to better reflect production-level database usage.
- **Random Forest** was selected due to its robustness and ability to handle feature importance.
- **Synthetic data** was generated because real churn datasets are rarely publicly available.


### Machine Learning
- Scikit-learn
- RandomForestClassifier
- NumPy
- Pandas
- Joblib / Pickle

### Frontend
- HTML5
- CSS3
- Bootstrap (custom styling)

## ▶️ How to Run Locally

Follow these steps to run the project on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShaniGupta4822/django-user-churn.git
cd django-user-churn

python -m venv venv

# Windows
venv\Scripts\activate


pip install django pymysql pandas numpy scikit-learn joblib


CREATE DATABASE churn_db;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'churn_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py seed_users

python manage.py runserver
Home → http://127.0.0.1:8000/
Admin → http://127.0.0.1:8000/admin/
Dashboard → http://127.0.0.1:8000/dashboard/


## 🚀 Future Improvements

- 🔐 User authentication & role-based access for dashboard
- 📡 Real-time churn monitoring using signals or Celery
- 📊 Advanced visualizations with Chart.js / Plotly
- 🤖 Automatic ML model retraining from admin panel
- ☁️ Deployment on AWS / Docker / Render
- 📱 Mobile-responsive dashboard UI
- 🔄 API-based architecture (Django REST Framework)

## 👨‍💻 Author

**Shani Gupta**  
Computer Science Undergraduate  

- 💻 Backend Development: Django, Python  
- 🤖 Machine Learning: Scikit-learn, Pandas  
- 🗄️ Database: MySQL  
- 📊 Data Structures & Algorithms  

Currently focused on strengthening backend development skills and
practical machine learning integration through real projects.



