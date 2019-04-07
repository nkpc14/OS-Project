from django.db import models


# Create your models here.

class Process(models.Model):
    name = models.CharField(max_length=255)
    arrivalTime = models.PositiveIntegerField(default=0)
    burstTime = models.PositiveIntegerField(default=0)
    completionTime = models.PositiveIntegerField(default=0)
    remainingTime = models.PositiveIntegerField(default=0)
    waitingTime = models.PositiveIntegerField(default=0)
    turnAroundTime = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.name) + "-" + str(self.pk)


class FacultyQueryManagement(models.Model):
    name = models.CharField(max_length=255, default="Faculty")
    quantumTime = models.PositiveIntegerField(default=0)
    time = models.TimeField(auto_now=True)
    noOfProcess = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.name) + "-" + str(self.pk)


class StudentQueryManagement(models.Model):
    name = models.CharField(max_length=255, default="Student")
    quantumTime = models.PositiveIntegerField(default=0)
    time = models.TimeField(auto_now=True)
    noOfProcess = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name) +"-" + str(self.pk)

