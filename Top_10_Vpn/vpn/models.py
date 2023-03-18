from django.db import models
import uuid
from django.core.validators import MaxValueValidator
# Create your models here.

class VpnList(models.Model):
    id = models.UUIDField(default= uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=200)
    logo = models.ImageField( upload_to='archivos',default=None)
    description = models.TextField(null = True,blank = True)
    specification = models.TextField(null = True,blank = True)
    offer = models.CharField(max_length=1000,null = True,blank = True)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(100)])
    website_url = models.URLField(max_length=1000,default=None)
    
    def __str__(self):
        return self.title
        
class All_avilable_filter(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Top_ten(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    type = models.ForeignKey(All_avilable_filter,on_delete=models.PROTECT)    
    First = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_first_set')    
    Second = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_second_set')    
    Third = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_third_set')    
    Forth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_forth_set')    
    Fifth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_fifth_set')    
    Sixth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_sexth_set')    
    Seventh = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_seventh_set')    
    Eighth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_eight_set')    
    Ninth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_ninth_set')    
    Tenth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_tenth_set')    

    def __str__(self):
        return str(self.id)

class Device(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.ForeignKey(All_avilable_filter,on_delete=models.CASCADE,)

    

class Location(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.ForeignKey(All_avilable_filter,on_delete=models.CASCADE)

   

class Service(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.ForeignKey(All_avilable_filter,on_delete=models.CASCADE)

                 
            

