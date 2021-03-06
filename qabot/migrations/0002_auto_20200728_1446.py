# Generated by Django 3.0.8 on 2020-07-28 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qabot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fqa',
            name='answer',
            field=models.TextField(max_length=500),
        ),
        migrations.CreateModel(
            name='SimilarProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('fqa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qabot.FQA')),
            ],
        ),
    ]
