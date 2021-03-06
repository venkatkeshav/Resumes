# Generated by Django 3.2.5 on 2021-07-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='pic',
            field=models.ImageField(default='static/images/play', upload_to='media/pics'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Branch',
            field=models.CharField(choices=[('ECE', 'ECE'), ('CSE', 'CSE')], help_text='Enter Your Branch', max_length=3),
        ),
    ]
