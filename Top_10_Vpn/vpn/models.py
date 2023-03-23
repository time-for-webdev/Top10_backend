from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError



# Create your models here.

class Specification(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    vpn_name = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return self.vpn_name

class remark(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    remarks = models.CharField(max_length=1000,default ="")
    
    def __str__(self):
        return self.remarks
    
class Comparision(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    vpn = models.CharField(max_length=1000,unique=True)
    comparison_description = models.TextField()
    moneybackguarantee = models.CharField(max_length=1000,default="")
    servers_or_countries= models.CharField(max_length=1000,default="")
    killswitch = models.CharField(max_length=1000,default="")
    number_of_device_or_licence = models.IntegerField(default=0)
    mobile = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.vpn

class VpnList(models.Model):
    id = models.UUIDField(default= uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=200,unique=True)
    logo = models.ImageField( upload_to='archivos',default="")
    description = models.TextField(null = True,blank = True)
    specification = models.ManyToManyField(Specification);
    remark = models.ForeignKey(remark,on_delete=models.PROTECT,null=True,blank = True)
    offer = models.CharField(max_length=1000,null = True,blank = True)
    rating = models.DecimalField(max_digits=3,decimal_places=1,default=0,validators=[MaxValueValidator(10)])
    website_url = models.URLField(max_length=1000,default="")
    riben_text = models.CharField(max_length=1000,null = True,blank=True)
    Comparision = models.OneToOneField(Comparision,null=True,blank = True,on_delete=models.PROTECT)
    user_name = models.CharField(max_length=1000,default="")
    user_comment = models.CharField(max_length=1000,default="")
    user_rating = models.DecimalField(max_digits=2,decimal_places=1,default=0,validators=[MaxValueValidator(5)])
    

    
    def __str__(self):
        return self.title
        
class All_avilable_filter(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Top_ten(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    type = models.OneToOneField(All_avilable_filter,on_delete=models.PROTECT,default="")    
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
    upadte_time = models.DateTimeField(auto_now_add=True,null =True,blank=True)


    def clean(self):
        # Check for duplicates in the First to Tenth fields
        first_to_tenth = [self.First, self.Second, self.Third, self.Forth, self.Fifth, self.Sixth, self.Seventh, self.Eighth, self.Ninth, self.Tenth]
        non_empty_fields = [field for field in first_to_tenth if field is not None]
        if len(non_empty_fields) != len(set(non_empty_fields)):
            raise ValidationError('The First to Tenth fields must be unique.')



    def __str__(self):
        return self.type.name


class Device(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.OneToOneField(All_avilable_filter,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name

    
    

    

class Location(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.OneToOneField(All_avilable_filter,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name

class Service(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    name = models.OneToOneField(All_avilable_filter,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name

class Form(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)     
    name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    Ques_comment = models.TextField(null=True,blank=True) 

    def __str__(self):
        return self.name  
    

