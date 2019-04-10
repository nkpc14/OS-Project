from django.db import models


# Create your models here.

class UserQueue(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name) + "-" + str(self.pk)

class QunatumTime(models.Model):
    quantumTime = models.PositiveIntegerField(default=2)

class Process(models.Model):
    name = models.CharField(max_length=255)
    arrivalTime = models.PositiveIntegerField(default=0)
    burstTime = models.PositiveIntegerField(default=0)
    completionTime = models.PositiveIntegerField(default=0)
    remainingTime = models.PositiveIntegerField(default=0)
    waitingTime = models.PositiveIntegerField(default=0)
    turnAroundTime = models.PositiveIntegerField(default=0)
    priority = models.BooleanField(default=0)
    user = models.ForeignKey(UserQueue, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + "-" + str(self.pk)


class Processed(models.Model):
    name = models.CharField(max_length=255)
    arrivalTime = models.PositiveIntegerField(default=0)
    burstTime = models.PositiveIntegerField(default=0)
    remainingTime = models.PositiveIntegerField(default=0)
    waitingTime = models.PositiveIntegerField(default=0)
    turnAroundTime = models.PositiveIntegerField(default=0)
    priority = models.BooleanField(default=0)
    user = models.ForeignKey(UserQueue, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + "-" + str(self.pk)

