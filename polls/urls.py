from django.urls import path

from . import views

app_name = "polls"

# This code block creates a list of URL rules. Whenever a URL is opened,
# Django finds the matching rule and runs the associated function.
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
