# Generated by Django 4.1.1 on 2022-10-07 14:43

import core.models
from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('first_name', core.models.LowerCase(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('last_name', core.models.LowerCase(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('user_img', models.ImageField(blank=True, null=True, upload_to='user')),
                ('password', models.CharField(max_length=150)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', core.models.LowerCase(max_length=100)),
                ('des', core.models.LowerCase(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address')),
                ('token', models.CharField(max_length=250)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_varified', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(to='core.permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Password_Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address')),
                ('token', models.CharField(max_length=250)),
                ('is_changed', models.BooleanField(default=False)),
                ('date_changed', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
