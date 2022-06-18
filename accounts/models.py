from django.db import models

Gender = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),  
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    gender = models.CharField(max_length=200,null=True,choices=Gender)
    phone = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contact_date']

    def __str__(self):
        return self.name