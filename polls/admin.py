from django.contrib import admin

from .models import Choice, Question


# TabularInline is a built-in Django feature that displays choices in a table.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Use QuestionAdmin so we can add choices on the same form as the question.
admin.site.register(Question, QuestionAdmin)
