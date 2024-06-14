from django.db import models


# About Model
class AboutMe(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
    
    def __str__(self):
        return "About Me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service Name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name