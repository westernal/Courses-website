from django.db import models
from django.db import models
from datetime import datetime

class course(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(default='', upload_to='store_image/', null=True)
    created_at = models.DateTimeField(default = datetime.now)


    def __str__(self):
        return self.name