import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        question = Question(pub_date=timezone.now() - datetime.timedelta(days=1, seconds=1))
        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        question = Question(pub_date=timezone.now() - datetime.timedelta(hours=23))
        self.assertIs(question.was_published_recently(), True)


def create_question(question_text, days):
    pub_date = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=pub_date)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question("Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        create_question("Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        past_question = create_question("Past question.", days=-30)
        create_question("Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [past_question])

    def test_two_past_questions(self):
        older = create_question("Older question.", days=-30)
        newer = create_question("Newer question.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [newer, older])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        question = create_question("Future question.", days=5)
        response = self.client.get(reverse("polls:detail", args=[question.pk]))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question("Past question.", days=-5)
        response = self.client.get(reverse("polls:detail", args=[question.pk]))
        self.assertContains(response, question.question_text)
