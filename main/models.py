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
