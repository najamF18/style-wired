# Generated by Django 3.2.5 on 2021-12-30 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='InitialProfileDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charateristic', models.CharField(choices=[('COMFORT', 'Comfort'), ('STYLE', 'Style'), ('Quality', 'Quality')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feelings', models.CharField(max_length=100)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, default=70, max_digits=5)),
                ('eye_color', models.CharField(choices=[('RED', 'Red'), ('GREEN', 'Green'), ('BLUE', 'Blue')], max_length=100)),
                ('hair_color', models.CharField(choices=[('BLONDE', 'Blonde'), ('BLACK', 'Black'), ('BROWN', 'Brown')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
