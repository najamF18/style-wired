# Generated by Django 3.2.5 on 2021-12-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_auto_20211229_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraTailoredSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neck', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
                ('waist', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
                ('bust', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
                ('hips', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
                ('shoulder', models.CharField(blank=True, choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
                ('inside_leg', models.CharField(blank=True, choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra-Large')], max_length=100)),
            ],
        ),
    ]