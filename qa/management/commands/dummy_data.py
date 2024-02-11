import random
from itertools import islice
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from qa.models import Question, Subject, Tag, SingleQuestion, QuestionMap, QuestionTag


class Command(BaseCommand):
    help = 'Generate dummy data for User and Question models'

    def add_arguments(self, parser):
        parser.add_argument('subject', type=int, help='Number of dummy users to create')
        parser.add_argument('questions', type=int, help='Number of dummy questions to create')
        parser.add_argument('singleQuestion', type=int, help='Number of dummy questions to create')
        parser.add_argument('tags', type=int, help='Number of dummy tag')

    def handle(self, *args, **options):
        subject = options['subject']
        questions = options['questions']
        sq = options['singleQuestion']
        tags = options['tags']



        batch_size = 100
        # objs = (Subject(title="Subject Title  %s" % i) for i in range(subject))
        # while True:
        #     batch = list(islice(objs, batch_size))
        #     if not batch:
        #         break
        #     subject_list = Subject.objects.bulk_create(batch, batch_size)
        #     print("bulk subject created...")
        #
        # # Generate Tag
        # objs = (Tag(name=get_random_string(20)) for i in range(tags))
        # while True:
        #     batch = list(islice(objs, batch_size))
        #     if not batch:
        #         break
        #     tag_list = Tag.objects.bulk_create(batch, batch_size)
        #     print("bulk tag created...")
        #
        # # Generate Question
        # objs = (Question(name="question Title  %s" % i, subject=subject_list[random.randint(0, len(subject_list)-1)]) for i in range(questions))
        # while True:
        #     batch = list(islice(objs, batch_size))
        #     if not batch:
        #         break
        #     question_list = Question.objects.bulk_create(batch, batch_size)
        #     print("bulk Question created...")
        #
        # # Generate Single Question
        # q_objs = []
        #
        #
        # for i in range(sq):
        #     print(i)
        #     q = SingleQuestion(title="Single Question Title  %s" % i)
        #
        #     q_objs.append(q)
        #
        # count = 0
        # for i in range(int(sq/batch_size)):
        #     q_batch = list(islice(q_objs, batch_size))
        #     print("batch len ", len(q_batch))
        #     if not q_batch:
        #         break
        #     SingleQuestion.objects.bulk_create(q_batch, batch_size, ignore_conflicts=True)
        #     count +=batch_size
        #     print("bulk single question created...", count)

        # Mapper
        # single_questions = SingleQuestion.objects.all()
        # sq_count = single_questions.count()
        # m_objs = []
        # t_objs = []
        # for q in single_questions:
        #     print(q.id)
        #     m = QuestionMap(question=question_list[random.randint(0, len(question_list) - 1)],
        #                                    single_question=q)
        #     t = QuestionTag.objects.create(single_question=q, tag=tag_list[random.randint(0, len(tag_list) - 1)])
        #     m_objs.append(m)
        #     t_objs.append(t)
        #
        # count = 0
        # for i in range(int(sq_count/batch_size)):
        #     m_batch = list(islice(m_objs, batch_size))
        #     t_batch = list(islice(t_objs, batch_size))
        #     if not m_batch:
        #         break
        #     QuestionMap.objects.bulk_create(m_batch, batch_size, ignore_conflicts=True)
        #     QuestionTag.objects.bulk_create(t_batch, batch_size, ignore_conflicts=True)
        #     count += batch_size
        #     print("bulk mapper created...", count)

        single_questions = SingleQuestion.objects.all()[100000:]
        single_question_count = single_questions.count()
        question_list = Question.objects.all()
        total_question = question_list.count()

        m_objs = []
        c = 0
        for q in single_questions:
            c+=1
            print(c)
            m = QuestionMap(question=question_list[random.randint(0, total_question - 1)], single_question=q)
            m_objs.append(m)

        count = 0
        for i in range(int(single_question_count/batch_size)):
            m_batch = list(islice(m_objs, batch_size))
            if not m_batch:
                break
            QuestionMap.objects.bulk_create(m_batch, batch_size, ignore_conflicts=True)
            count += batch_size
            print("bulk mapper created...", count)





        self.stdout.write(self.style.SUCCESS(f'Dummy question created: {count}'))