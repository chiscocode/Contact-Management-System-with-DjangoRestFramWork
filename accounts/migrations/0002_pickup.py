# Generated by Django 4.0.5 on 2022-06-07 12:43

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('sendername', models.CharField(max_length=200)),
                ('recivername', models.CharField(max_length=200)),
                ('senderemail', models.CharField(max_length=200)),
                ('reciveremail', models.CharField(max_length=200)),
                ('senderphone', models.CharField(max_length=200)),
                ('reciverphone', models.CharField(max_length=200)),
                ('senderaddress', models.CharField(max_length=200)),
                ('reciveraddress', models.CharField(max_length=200)),
                ('parcel', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pickup', 'PICKUP'), ('processing', 'PROCESSING'), ('delivered', 'DELIVERED')], max_length=200)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-request_date'],
            },
        ),
    ]
