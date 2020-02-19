from django.db import models
from committees.models import Committee


class Staff(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField()
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='staff', blank=True, null=True)

    def __str__(self):
        return self.name

    def committee_position(self):
        return self.positions.filter(branches__name='Committee Staff')

    def secretariat_position(self):
        return self.positions.filter(branches__name='Secretariat')

    def digital_press_team_position(self):
        return self.positions.filter(branches__name='Digital Press Team')

    def conference_services_position(self):
        return self.positions.filter(branches__name='Conference Services')


class Position(models.Model):
    name = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(default=1)
    staff = models.ManyToManyField(Staff, related_name='positions', blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=200)
    position = models.ManyToManyField(Position, related_name='branches', blank=True)

    def __str__(self):
        return self.name
