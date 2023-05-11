from django.db import models
from ckeditor.fields import RichTextField


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

    class Meta:
        verbose_name = 'Imtihon'
        verbose_name_plural = 'Imtihonlar'
