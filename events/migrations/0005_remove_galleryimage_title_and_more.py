# Generated by Django 5.0 on 2023-12-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_event_type_gallery_galleryimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='uploaded_time',
            field=models.DateTimeField(null=True),
        ),
    ]
