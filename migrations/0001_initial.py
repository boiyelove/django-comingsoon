# Generated by Django 4.0.4 on 2022-05-03 21:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComingSoonNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('verification_link', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]