# Generated by Django 3.2.5 on 2021-07-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0004_alter_candidate_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='', help_text='Select your gender', max_length=6),
        ),
    ]