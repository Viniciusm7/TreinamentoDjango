from django.contrib import admin
from .models import Question
from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceInline(admin.TabularInline):
    #...


class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
# Register your models here.
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    fields = ['pub_date', 'question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]



admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)