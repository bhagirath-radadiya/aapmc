from django.db import models

class PriceMaster(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    category = models.CharField(max_length=50, db_index=True)
    high = models.FloatField(db_index=True, null=True)
    low = models.FloatField(db_index=True, null=True)
    average = models.FloatField(db_index=True, null=True)
    date = models.DateField(db_index=True)