from django.db import models

# Create your models here.

class Video(models.Model):
    vd_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    vd_file = models.FileField(upload_to='videos/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vd_name