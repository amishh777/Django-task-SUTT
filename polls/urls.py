from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # These routes now point to class-based views through as_view().
    path("", views.IndexView.as_view(), name="index"),
    # Changed question_id to pk because Django's built-in DetailView
    # looks for an argument named pk to find the question.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
