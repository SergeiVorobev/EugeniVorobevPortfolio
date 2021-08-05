# Generated by Django 3.2.6 on 2021-08-05 20:47

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
            name='MyApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('desc', models.TextField(blank=True, default='')),
                ('image', models.ImageField(upload_to='my_apps')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_apps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'my apps',
                'ordering': ['name'],
            },
        ),
    ]
