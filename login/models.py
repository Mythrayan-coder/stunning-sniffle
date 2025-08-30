from django.db import models




class table(models.Model):
    Full_Name = models.CharField(max_length=100)
    Email_address = models.CharField(max_length=100)
    Password = models.TextField()
    Confirm_Password = models.TextField()
     

    
    
