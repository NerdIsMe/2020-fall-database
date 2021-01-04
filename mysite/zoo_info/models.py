from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length =30) # 姓名
    #birth = models.DateField() # 出生年月日
    gender = models.CharField(max_length =1) # 生理性別
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)


# Zoo database
# zoo database - strong entity
class Zoo(models.Model):
    zoo_id = models.CharField(max_length = 30, primary_key = True)
    number_of_visitors = models.IntegerField()
    number_of_sites = models.IntegerField()
    number_of_categories = models.IntegerField()
    avg_temp = models.FloatField()
    ticket_price = models.IntegerField()
    rain_per_year = models.FloatField()

class Area(models.Model):
    area_id = models.CharField(max_length = 30, primary_key = True)#
    position = models.CharField(max_length = 30)#
    nearby = models.CharField(max_length = 30)#
    theme = models.CharField(max_length = 30)#
    close_time = models.CharField(max_length = 30)#
    distance = models.FloatField()
    zoo_id = models.ForeignKey(Zoo, on_delete = models.CASCADE)

class Habitat(models.Model):
    H_id = models.CharField(max_length = 30, primary_key = True)
    weather = models.CharField(max_length = 30)
    continent = models.CharField(max_length = 30)
    terrian = models.CharField(max_length = 30)

class Animal(models.Model):
    scientific_id = models.CharField(max_length = 30, primary_key = True)
    animal_name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30)
    conservation = models.CharField(max_length = 30)
    h_id = models.ForeignKey(Habitat, on_delete = models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete = models.CASCADE)

class IndividualAnimal(models.Model):
    idividual_id = models.CharField(max_length = 30, primary_key = True)
    age = models.IntegerField()
    year_in = models.IntegerField()
    animal_id = models.ForeignKey(Animal, on_delete = models.CASCADE)

class Zookeeper(models.Model):
    keeper_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    join_time = models.IntegerField()
    department = models.CharField(max_length = 30)
    birth = models.IntegerField()

