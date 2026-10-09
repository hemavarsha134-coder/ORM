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


