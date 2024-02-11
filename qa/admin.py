from django.contrib import admin
from .models import Tag, QuestionTag, SingleQuestion, Question, QuestionMap, Subject


admin.site.register(Tag)
admin.site.register(QuestionTag)
admin.site.register(SingleQuestion)
admin.site.register(Question)
admin.site.register(QuestionMap)
admin.site.register(Subject)
