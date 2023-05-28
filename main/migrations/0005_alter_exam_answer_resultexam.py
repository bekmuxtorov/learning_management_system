# Generated by Django 4.2 on 2023-05-26 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_remove_exam_topic_exam_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='answer',
            field=models.CharField(choices=[('answer_a', 'A javob'), ('answer_b', 'B javob'), ('answer_c', 'C javob'), ('answer_d', 'D javob')], default='answer_a', max_length=10, verbose_name='Javob'),
        ),
        migrations.CreateModel(
            name='ResultExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_question', models.IntegerField(blank=True, null=True, verbose_name='Jami savollar')),
                ('wrong', models.IntegerField(verbose_name='Xato javoblar')),
                ('correct', models.IntegerField(verbose_name="To'g'ri javoblar")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_exam', to='main.department', verbose_name="Bo'lim")),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='result_exam', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Natija',
                'verbose_name_plural': 'Natijalar',
            },
        ),
    ]