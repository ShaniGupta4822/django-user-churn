
import os
import pickle
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import UserActivity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "churn_model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))


def home(request):
    if request.method == "POST":
        request.session["user_input"] = {
            "lc": int(request.POST["login_count"]),
            "ast": float(request.POST["avg_session_time"]),
            "di": int(request.POST["days_inactive"]),
            "fu": int(request.POST["feature_usage"]),
        }
        return redirect("dashboard")

    return render(request, "home.html")


def dashboard(request):
    user_result = None
    user_input = request.session.pop("user_input", None)

    if user_input:
        features = [[
            user_input["lc"],
            user_input["ast"],
            user_input["di"],
            user_input["fu"]
        ]]

        prob = model.predict_proba(features)[0][1]
        churn = int(prob * 100)

        if churn >= 70:
            risk = "HIGH"
        elif churn >= 40:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        user_result = {
            "churn": churn,
            "risk": risk
        }

    search = request.GET.get("search", "")
    qs = UserActivity.objects.all()

    if search:
        qs = qs.filter(user_id__icontains=search)

    users = []
    for u in qs:
        prob = model.predict_proba([[
            u.login_count,
            u.avg_session_time,
            u.days_inactive,
            u.feature_usage
        ]])[0][1]

        churn = int(prob * 100)
        risk = "high" if churn >= 70 else "medium" if churn >= 40 else "low"

        users.append({
            "user_id": u.user_id,
            "login_count": u.login_count,
            "days_inactive": u.days_inactive,
            "feature_usage": u.feature_usage,
            "churn_prob": churn,
            "risk": risk
        })

    paginator = Paginator(users, 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    feature_names = ["Login Count", "Avg Session Time", "Days Inactive", "Feature Usage"]
    feature_importance = [
        {"name": n, "score": int(s * 100)}
        for n, s in zip(feature_names, model.feature_importances_)
    ]

    feature_importance.sort(key=lambda x: x["score"], reverse=True)

    return render(request, "dashboard.html", {
        "user_result": user_result,
        "page_obj": page_obj,
        "feature_importance": feature_importance,
        "search": search
    })
