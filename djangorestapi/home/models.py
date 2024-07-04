from django.db import models

# Create your models here.
class Team(models.Model):
    team_name= models.CharField(max_length=20)

    def __str__(self) ->str:
        return self.team_name
    

class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    location=models.CharField(max_length=100)
    team=models.ForeignKey(Team,null=True,blank=True,on_delete=models.CASCADE,related_name="members",default=None)