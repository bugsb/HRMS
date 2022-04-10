from django.db import models

# Create your models here.
class GM(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    sales = models.IntegerField()
    commission = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name

class RGM(models.Model):
    id = models.AutoField(primary_key=True)
    GM_id = models.ForeignKey(GM,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    sales = models.IntegerField()
    commission = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name

class AGM(models.Model):
    id = models.AutoField(primary_key=True)
    RGM_id = models.ForeignKey(RGM,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    sales = models.IntegerField()
    commission = models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.name

class DM(models.Model):
    id = models.AutoField(primary_key=True)
    AGM_id = models.ForeignKey(AGM,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    sales = models.IntegerField()
    commission = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name