from __future__ import unicode_literals

from django.urls import reverse

from django.db import models

class Action(models.Model):
    position = models.ForeignKey('Position', related_name='pos_type')
    action = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.action

class Position(models.Model):
    POSITION_TYPES = (
        ("Producer", "Producer"),
        ("Actor", "Actor"),
        ("Dancer", "Dancer"),
        ("Designer", "Designer"),
        ("Other", "Other Cool Person")
    )
    position = models.CharField(max_length=32, choices=POSITION_TYPES)

    def __str__(self):
        return "%s" % (self.position)

class Project(models.Model):
    creation_data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return "%s" % self.name

class Student(models.Model):
    position = models.ForeignKey('Position')
    action = models.ForeignKey('Action')
    project = models.ForeignKey('Project', related_name='students', blank=True, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=2048)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

    def get_absolute_url(self):
            return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s %s : %s" % (self.fname, self.lname, self.position)
