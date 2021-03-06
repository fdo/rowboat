from django.db import models

class Running(models.Model):
    data = models.CharField('notes', max_length=200)
    minutes = models.IntegerField()
    timeenter = models.DateTimeField('timeenter')    
   
class Weight(models.Model):
    data = models.CharField('notes', max_length=200)
    damage = models.DecimalField(max_digits=4, decimal_places=1)
    timeenter = models.DateTimeField('timeenter')
   
class Reps(models.Model):
    exercise = models.CharField('exercisetype', max_length=60)
    reps = models.IntegerField()
    more = models.CharField('morenotes', max_length=200)
    timeenter = models.DateTimeField('timeenter')

class PoliceReport(models.Model):
    offense = models.CharField('Offense', max_length=60)
    license_number = models.CharField('plates', max_length=10)
    Details = models.TextField('Details', max_length=2048)
    timeenter = models.DateTimeField('timeenter')
   
class Thoughts(models.Model):
    title= models.CharField('Title', max_length=60)
    author = models.CharField('Author', max_length=30)
    details = models.TextField('Details', max_length=2048)
    timeenter = models.DateTimeField('TimeEnter')
   
    def __str__(self):
         return '%s' % (self.exercise)
