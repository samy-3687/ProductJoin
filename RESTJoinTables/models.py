from django.db import models

class JoinTablesmodel(models.Model):
    prd_name = models.CharField(max_length = 50)
    prd_cat = models.CharField(max_length = 50)
    prd_price = models.IntegerField()
    prd_id = models.IntegerField(primary_key = True)
    prd_desc = models.CharField(max_length = 500)