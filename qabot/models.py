from django.db import models

# Create your models here.
from django.utils.html import format_html


class FQA(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=500)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    def html_answer(self):
        return format_html(self.answer)


class FQA_COPY(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=500)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    def html_answer(self):
        return format_html(self.answer)

    class Meta:
        db_table = 'qabot_fqa_copy1'


class SimilarQuestion(models.Model):
    question = models.CharField(max_length=200)
    fqa = models.ForeignKey(FQA, on_delete=models.CASCADE, related_name="sq", limit_choices_to={'valid': True})

    class Meta:
        db_table = 'qabot_similar_question'
