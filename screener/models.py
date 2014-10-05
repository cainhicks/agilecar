from django.db import models



# Create your models here.
class Screener(models.Model):
    name = models.CharField(max_length = 128)
    
    #questions = models.ManyToManyField(ScreenerQuestion)

    def __init__(self, *args, **kwargs):
        #extra = kwargs.pop('extra')
        super(Screener, self).__init__(*args, **kwargs)

    def save_screeners(self, questions):
        self.save()
        for question_key, question_value in questions.items():
            sq = ScreenerQuestion()
            sq.screener = self
            sq.question_text = question_value[question_key]
            sq.save()
            if len(question_value) > 1:
                first = True
                for k, v in question_value.items():
                    if not first:
                        sa = ScreenerAnswer()
                        sa.screener_question = sq
                        sa.answer = v
                        sa.save()
                    else:
                        first = False



class ScreenerQuestion(models.Model):
    QUESTION_TYPES = (
                      ('ff', 'Free Form'),
                      ('mc', 'Multiple Choice')
                      )
    question_text = models.CharField(max_length = 256)
    #question_type = models.CharField(max_length = 2, choices = QUESTION_TYPES)
    #order = models.IntegerField()
    #answers = models.ManyToManyField(ScreenerAnswer)
    screener = models.ForeignKey(Screener, null = True)

class ScreenerAnswer(models.Model):
    screener_question = models.ForeignKey(ScreenerQuestion, null = True)
    answer = models.CharField(max_length = 512)
    #order = models.IntegerField()


class ScreenerResponse(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(ScreenerResponse, self).__init__(*args, **kwargs)
        from application.models import Application
        self.screener_question = models.ForeignKey(ScreenerQuestion)
        self.response = models.CharField(max_length = 1024)
        self.application = models.ForeignKey(Application, null = True)
        self.screener = models.ForeignKey(Screener)



def load_screener(id):
    screener = Screener.objects.get(id = id)
    questions = ScreenerQuestion.objects.filter(screener__id = screener.id)
    for question in questions:
        question.answers = ScreenerAnswer.objects.filter(screener_question__id = question.id)
    screener.questions = questions
    return screener