# HTTP responses. Something that Django provides and calling it creates a response object.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # The render function fills the HTML template with question data and returns the page
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(
        f"You're looking at the results of question {question_id}."
    )


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
