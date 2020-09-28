from django.db import models

class Questions(models.Model):
    ques_type = (
        ('Text'),
        ('MCQ'),
    )
    ques_no     = models.IntegerField()
    slot        = models.IntegerField(default=0)
    ques        = models.CharField(maxlength=50)
    option      = models.CharField(maxlength=1)
    type_ques   = models.ChoiceField(choices=ques_type)
    correct_ans = models.CharField(maxlength=50)
