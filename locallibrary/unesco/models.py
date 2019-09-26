from django.db import models

# Create your models here.
class Category(models.Model) :
    category1 = models.CharField(max_length=128)
    #states2 = models.ManyToManyField('States', through='Site')
    def __str__(self) :
        return self.name

class States(models.Model) :
    states1 = models.CharField(max_length=128)
    #category1 = models.ManyToManyField('Category', through='Site')
    def __str__(self) :
        return self.name

class Region(models.Model) :
     region1 = models.CharField(max_length=128)

     def __str__(self) :
       return self.name

class Iso(models.Model) :
     iso1 = models.CharField(max_length=128)

     def __str__(self) :
       return self.name

class Site(models.Model):
    name = models.CharField(max_length=128,null=True)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    description = models.CharField(max_length=128,null=True)
    justification = models.CharField(max_length=128,null=True)
    longitude = models.CharField(max_length=128,null=True)
    latitude = models.CharField(max_length=128,null=True)
    area_hectares = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name