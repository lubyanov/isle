# Generated by Django 2.0.7 on 2018-08-08 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0029_auto_20180808_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_type', models.SmallIntegerField(blank=True, choices=[(1, 'Автор интересных вопросов'), (2, 'Другое'), (3, 'Результаты тестов'), (4, 'Результат выполнения'), (5, 'Лидер мнений'), (6, 'Презентация с оценкой ведущего'), (7, 'Результаты эксперимента'), (8, 'Обратная связь участников (start-stop-continue)'), (9, 'Обратная связь тьютора\\ментора (start-stop-continue)')], null=True, verbose_name='Тип результата')),
                ('rating', models.SmallIntegerField(blank=True, choices=[(1, 'слабый результат'), (2, 'нормальный результат'), (3, 'отличный результат')], null=True, verbose_name='Оценка')),
                ('competences', models.CharField(blank=True, default='', max_length=300, verbose_name='Продемонстрированные компетенции')),
                ('result_comment', models.CharField(blank=True, default='', max_length=1000, verbose_name='Комментарии сборщика')),
                ('group_dynamics', models.CharField(blank=True, default='', max_length=300, verbose_name='Групповая динамика')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Event')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.SmallIntegerField(blank=True, choices=[(1, 'Лидер'), (2, 'Участник')], null=True)),
                ('team_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.TeamResult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teamresult',
            name='user_roles',
            field=models.ManyToManyField(through='isle.UserRole', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventteammaterial',
            name='result',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.TeamResult'),
        ),
        migrations.AlterUniqueTogether(
            name='userrole',
            unique_together={('user', 'team_result')},
        ),
    ]
