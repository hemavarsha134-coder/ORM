# Ex02 Django ORM Web Application
## Date: 09/10/2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    Order_No=models.IntegerField(primary_key=True)
    Product_Name=models.CharField(max_length=15)
    Product_Quantity=models.IntegerField()
    Price=models.FloatField()
    Mobile_No=models.IntegerField()
    Customer_Name=models.CharField(max_length=15)
    Address=models.TextField()

class BlinkitAdmin(admin.ModelAdmin):
    list_display=["Order_No","Product_Name","Product_Quantity","Price","Mobile_No","Customer_Name","Address"]





admin.py
from django.contrib import admin
from.models import Blinkit,BlinkitAdmin
admin.site.register(Blinkit,BlinkitAdmin)

```


## OUTPUT
![alt text]({1BE3C2DE-E143-4413-B6E3-AAD10B40ACBA}.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
