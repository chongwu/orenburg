from django.db import models


class Department(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.fio


class Staff(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now_add=True)
    date_fired = models.DateField(null=True, blank=True)
