from django.db import models
from shortuuidfield import ShortUUIDField


Status = (
    ('pickup', 'PICKUP'),
    ('processing', 'PROCESSING'),
    ('delivered', 'DELIVERED'),
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contact_date']

    def __str__(self):
        return self.name

class Pickup(models.Model):
    uuid = ShortUUIDField(null=True)
    sendername = models.CharField(max_length=200,null=False)
    recivername = models.CharField(max_length=200,null=False)
    senderemail = models.CharField(max_length=200,null=False)
    reciveremail = models.CharField(max_length=200,null=False)
    senderphone = models.CharField(max_length=200,null=False)
    reciverphone = models.CharField(max_length=200,null=False)
    senderaddress = models.CharField(max_length=200,null=False)
    reciveraddress = models.CharField(max_length=200,null=False)
    parcel = models.TextField(blank=True)
    status=models.CharField(max_length=200,null=True,choices=Status)
    request_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-request_date']

    def __str__(self):
        return self.uuid