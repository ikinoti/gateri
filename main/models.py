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
