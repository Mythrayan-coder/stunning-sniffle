from django.db import models

#class coolie(models.Model):
#    Email = models.CharField(max_length=100)
#    Password = models.TextField()


class chepak(models.Model):
    Full_Name = models.CharField(max_length=100)
    Email_address = models.CharField(max_length=100)
    Password = models.TextField()
    Confirm_Password = models.TextField()
     

    
    
