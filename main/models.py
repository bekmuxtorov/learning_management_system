from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Bo\'lim nomi')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Bo\'lim'
        verbose_name_plural = 'Bo\'limlar'

    def get_topic(self):
        return self.topics.all()


class Topic(models.Model):
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        verbose_name='Bo\'lim',
        related_name='topics'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Mavzu nomi'
    )
    body = RichTextField(verbose_name='Mavzu matni')
    video_url = models.URLField(
        verbose_name='Video manzil',
        blank=True, null=True
    )
    tasks = RichTextField(verbose_name='Vazifalar')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Mavzu'
        verbose_name_plural = 'Mavzular'

    def get_resources(self):
        return self.resources.all()


class Resource(models.Model):
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
        verbose_name='Mavzu',
        related_name='resources'
    )
    name = models.CharField(max_length=255, verbose_name='Resurs nomi')
    file = models.FileField(upload_to='resources', verbose_name='Fayl')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Resurs'
        verbose_name_plural = 'Resurslar'


class Exam(models.Model):
    ANSWERS = (
        ('answer_a', 'A javob'),
        ('answer_b', 'B javob'),
        ('answer_c', 'C javob'),
        ('answer_d', 'D javob')
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='exams_department'
    )
    question = models.TextField(
        verbose_name='Savol'
    )
    answer_a = models.CharField(
        verbose_name='A javob:',
        max_length=400
    )
    answer_b = models.CharField(
        verbose_name='b javob:',
        max_length=400
    )
    answer_c = models.CharField(
        verbose_name='C javob:',
        max_length=400
    )
    answer_d = models.CharField(
        verbose_name='D javob:',
        max_length=400
    )
    answer = models.CharField(
        verbose_name='Javob',
        max_length=10,
        choices=ANSWERS,
        default='answer_a'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department.name + ' || ' + str(self.id)

    def get_answer(self):
        answers = {
            'answer_a': self.answer_a,
            'answer_b': self.answer_b,
            'answer_c': self.answer_c,
            'answer_d': self.answer_d
        }
        return answers.get(self.answer)

    class Meta:
        verbose_name = 'Imtihon'
        verbose_name_plural = 'Imtihonlar'


class ResultExam(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='result_exam',
        verbose_name='User'
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        related_name='result_exam',
        verbose_name='Bo\'lim'
    )
    total_question = models.IntegerField(
        verbose_name='Jami savollar', blank=True, null=True)
    wrong = models.IntegerField(verbose_name='Xato javoblar')
    correct = models.IntegerField(verbose_name='To\'g\'ri javoblar')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' | ' + self.department.name

    def save(self, *args, **kwargs):
        self.total_question = self.department.exams_department.count()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Natija'
        verbose_name_plural = 'Natijalar'
