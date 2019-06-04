from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{0}, Date: {1}'.format(self.question_text, str(self.pub_date))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '\nQuestion: {0},\nChoice: {1}, Votes: {2}\n'.format(
            self.question,
            self.choice_text,
            self.votes
        )
