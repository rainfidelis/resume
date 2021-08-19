from django.db import models


class ContactModel(models.Model):

    name = models.CharField('Name', max_length=200) 
    email = models.EmailField('Email Address')
    subject = models.CharField('Subject', max_length=200)
    message = models.TextField('Message Body')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name