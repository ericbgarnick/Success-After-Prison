from django.db import models


# Create your models here.
class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resouce_link = models.URLField()


class DemoModel(models.Model):
    demo_field = models.CharField(max_length=50)

