from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=50)
    blog= models.CharField(max_length=1000)
    created_at=models.DateField()
    

    def __str__(self):
        return self.name