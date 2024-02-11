from django.db import models

"""
    Used separate Join table Approach for ManyToMany relation.  With the join table approach, we have more control over the database schema and indexing. 
    This allows for better optimization of queries, making it more scalable for handling large volumes of data
"""


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
    """
    Join table for Question and SingleQuestion ManyToMany relation
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # db_index=True not needed for ForeignKey
    single_question = models.ForeignKey(SingleQuestion, on_delete=models.CASCADE)


class QuestionTag(models.Model):
    """
    Join table for SingleQuestion and Tag ManyToMany Relation
    """
    single_question = models.ForeignKey(SingleQuestion, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
