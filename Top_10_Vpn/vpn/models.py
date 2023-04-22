from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
import pycountry
import datetime



# global tuples 

All_Device = (
    ('Andriod','Andriod'),
    ('iPhone&iPad','iPhone&iPad'),
    ('Mac','Mac'),
    ('Routers','Routers'),
    ('Pc','Pc'),
    ('Windows','Windows')
    )


today = datetime.date.today()
year = today.strftime("%Y")
All_Service_obj = 'Overall Best Vpn of '+year
All_Service = [
    [All_Service_obj,All_Service_obj],
] 


All_Locations=[]
for i in range(0,len(pycountry.countries)):
    country = list(pycountry.countries)[i].name 
    flag_code = list(pycountry.countries)[i].flag
    All_Locations += [[country,country]]

All_cateogry = (
    ('Privacy','Privacy'),
    ('Speed','Speed'),
    ('security','Security'),
    ('Newbies','Newbies'),
)

    






# Create your models here.

class Specification(models.Model):
    
    vpn_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.vpn_name

class remark(models.Model):
    
    remarks = models.CharField(max_length=200,default ="")
    
    def __str__(self):
        return self.remarks
    
class Comparision(models.Model):
    
    vpn = models.CharField(max_length=200,unique=True)
    comparison_description = models.TextField()
    moneybackguarantee = models.CharField(max_length=200,default="")
    servers_or_countries= models.CharField(max_length=200,default="")
    killswitch = models.CharField(max_length=200,default="")
    ChargePerMonth = models.IntegerField(default=0)
    number_of_device_or_licence = models.IntegerField(default=0)
    mobile = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.vpn


class feature(models.Model):
    category = models.CharField(max_length=200,choices =All_cateogry,default=1,unique=True)
    def __str__(self):
        return self.category


class VpnList(models.Model):
    id = models.UUIDField(default= uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=200,unique=True)
    logo = models.ImageField( upload_to='archivos',default="")
    icon = models.ImageField(upload_to='archivos',default="")
    description = models.TextField(null = True,blank = True)
    specification = models.ManyToManyField(Specification);
    remark = models.ForeignKey(remark,on_delete=models.PROTECT,null=True,blank = True)
    offer = models.CharField(max_length=200,null = True,blank = True)
    rating = models.DecimalField(max_digits=3,decimal_places=1,default=0,validators=[MaxValueValidator(10)])
    website_url = models.URLField(max_length=200,default="")
    riben_text = models.CharField(max_length=200,null = True,blank=True)
    Comparision = models.OneToOneField(Comparision,default="",on_delete=models.PROTECT)
    user_name = models.CharField(max_length=200,default="")
    feature = models.ManyToManyField(feature)
    user_comment = models.CharField(max_length=200,default="")
    user_rating = models.DecimalField(max_digits=2,decimal_places=1,default=0,validators=[MaxValueValidator(5)])

  

    
    def __str__(self):
        return self.title
        





class Device(models.Model):
       
    name = models.CharField(max_length=200,unique = True,choices=All_Device)

     
    First = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_first_set')    
    Second = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_second_set')    
    Third = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_third_set')    
    Forth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_forth_set')    
    Fifth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_fifth_set')    
    Sixth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_sexth_set')    
    Seventh = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_seventh_set') 
    Eighth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_eighth_set')    
    Nineth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_nineth_set')    
    Tenth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_tenth_set')      

    upadte_time = models.DateTimeField(auto_now_add=True,null =True,blank=True)


    def clean(self):
        # Check for duplicates in the First to Tenth fields
        first_to_tenth = [self.First, self.Second, self.Third, self.Forth, self.Fifth, self.Sixth, self.Seventh,self.Seventh,self.Eighth,self.Nineth,self.Tenth]
        non_empty_fields = [field for field in first_to_tenth if field is not None]
        if len(non_empty_fields) != len(set(non_empty_fields)):
            raise ValidationError('The First to Tenth fields must be unique.')

    def __str__(self):
        return self.name 

    

    

class Location(models.Model):
    
    
    name = models.CharField(unique=True,max_length= 200,choices=All_Locations)
    

       
    First = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_1_set')    
    Second = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_2_set')    
    Third = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_3_set')    
    Forth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_4_set')    
    Fifth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_5_set')    
    Sixth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_6_set')    
    Seventh = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_7_set')    

    upadte_time = models.DateTimeField(auto_now_add=True,null =True,blank=True)


    def clean(self):
        # Check for duplicates in the First to Tenth fields
        first_to_tenth = [self.First, self.Second, self.Third, self.Forth, self.Fifth, self.Sixth, self.Seventh]
        non_empty_fields = [field for field in first_to_tenth if field is not None]
        if len(non_empty_fields) != len(set(non_empty_fields)):
            raise ValidationError('The First to Tenth fields must be unique.')


    
    def __str__(self):
        return pycountry.countries.get(name = self.name).flag + " " + self.name 

class Service(models.Model):
    
    name = models.CharField(unique=True,max_length=200,choices=All_Service)

    First = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_1st_set')    
    Second = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_2nd_set')    
    Third = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_3rd_set')    
    Forth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_4th_set')    
    Fifth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_5th_set')    
    Sixth = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_6th_set')    
    Seventh = models.ForeignKey(VpnList,on_delete=models.PROTECT,null=True,blank=True,related_name='top_ten_7th_set')    

    upadte_time = models.DateTimeField(auto_now_add=True,null =True,blank=True)


    def clean(self):
        # Check for duplicates in the First to Tenth fields
        first_to_tenth = [self.First, self.Second, self.Third, self.Forth, self.Fifth, self.Sixth, self.Seventh]
        non_empty_fields = [field for field in first_to_tenth if field is not None]
        if len(non_empty_fields) != len(set(non_empty_fields)):
            raise ValidationError('The First to Tenth fields must be unique.')
    

    def __str__(self):
        return self.name

class Form(models.Model):
         
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    Ques_comment = models.TextField(null=True,blank=True) 

    def __str__(self):
        return self.name  


class FAQ(models.Model):
    Question = models.CharField(max_length=200,default="",unique=True)
    Answer =  models.TextField(default="")

    def __str__(self):
        return 'Question '+str(self.id)

class OwnerContactDetails(models.Model):
    owner = (
        ('admin','admin'),
        ('user1', 'user1'),
        ('user2', 'user2'),
    )
    
    name = models.CharField(max_length=200,default="",choices=owner,unique=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Facebook = models.URLField(max_length=200,null=True,blank=True)
    Twitter = models.URLField(max_length=200,null=True,blank=True)
    Youtube = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name



        




    

