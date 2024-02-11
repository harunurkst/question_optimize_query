import random
from itertools import islice
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from qa.models import Question, Subject, Tag, SingleQuestion, QuestionMap, QuestionTag
from qa.models import Tag, QuestionTag, SingleQuestion, Question, QuestionMap


class Command(BaseCommand):
    help = 'Generate dummy data for User and Question models'

    def handle(self, *args, **options):
        QuestionTag.objects.all().delete()
        QuestionMap.objects.all().delete()
        Tag.objects.all().delete()
        SingleQuestion.objects.all().delete()
        Question.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'Dummy data deleted'))
