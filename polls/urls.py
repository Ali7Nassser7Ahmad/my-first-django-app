from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.ListQuestionView.as_view(), name="index"),
    path("question/<int:pk>/", views.DetailQuestionView.as_view(), name="detail"),
    path("question/<int:pk>/vote", views.VoteQuestionView.as_view(), name="vote"),
    path("question/<int:pk>/results", views.ResultQuestionView.as_view(), name="results"),
]