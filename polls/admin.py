from django.contrib import admin

from .models import Choice, Question


# TabularInline is a built-in Django feature that displays choices in a table.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


# Use QuestionAdmin so we can add choices on the same form as the question.
admin.site.register(Question, QuestionAdmin)
