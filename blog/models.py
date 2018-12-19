from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Organization(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=200,null=True, blank=True, default='Address')
    img = models.CharField(default='../media/org.jpg', max_length=300)

    def __str__(self):
        return self.name

class Hackathon(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    date = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)
    img = models.CharField(default='../media/hack.jpg', max_length=300)

    def __str__(self):
        return self.name

class User(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)
    img = models.CharField(default='../media/user.jpg', max_length=300)

    def __str__(self):
        return self.name



class Team(models.Model):
    img = models.CharField(default='../media/team.png', max_length=300)
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    created_date = models.DateField(default=datetime.date.today)
    max = models.IntegerField(default=5, null = True, blank = True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    likes = models.IntegerField( null=True, blank=True, default=0)
    created_date = models.DateField(default=datetime.date.today)
    img = models.CharField(default='../media/proj.jpg', max_length=300)

    def __str__(self):
        return self.name

class UserTeam(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.team)

class OrgHack(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True)
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (str(self.organization) + str('-') + str(self.hackathon))

class UserTeamHack(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (str(self.team) + str('-') + str(self.hackathon))

class UserTeamProject(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (str(self.team) + str('-') + str(self.project))

class Role(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    level = models.IntegerField(default=3,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    description = models.TextField( null=True, blank=True, default='Description')

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.role)

class Speaker(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')

    def __str__(self):
        return self.name

class SectionHack(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.section)
