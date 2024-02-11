from django.shortcuts import render
from django.db.models import Count

from qa.models import SingleQuestion, Subject


def question_count(request):
    """
    Time: 197 MS for 10 subjects

    """
    subjects = Subject.objects.all()[2470:2480]
    subject_ids = [s.id for s in subjects]

    # Query to count SingleQuestions filtered by Subject IDs and Tags starting with 'a'
    count_single_questions = SingleQuestion.objects.filter(
        questionmap__question__subject__id__in=subject_ids,
        questiontag__tag__name__istartswith='a'
    ).annotate(total_count=Count('id')).aggregate(total_count=Count('total_count'))

    total_count = count_single_questions['total_count']
    return render(request, 'counter.html', {'count': total_count})
