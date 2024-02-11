from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # db_index=True not needed for unique field, auto indexed

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # db_index=True not needed for ForeignKey

    def __str__(self):
        return f"{self.name} - {self.subject.id}"


class SingleQuestion(models.Model):
    title = models.CharField(max_length=150)


class QuestionMap(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # db_index=True not needed for ForeignKey
    single_question = models.ForeignKey(SingleQuestion, on_delete=models.CASCADE)


class QuestionTag(models.Model):
    single_question = models.ForeignKey(SingleQuestion, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
