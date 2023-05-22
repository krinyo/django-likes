from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField('Местоположение', max_length=50)
    main_image = models.ImageField(upload_to='location_images/', null=True)
    like_image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    dislike_image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = "Местоположения"

class Rating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField()
    dislike = models.BooleanField()

    def __str__(self):
        date_formatted = self.date_created.strftime("%d.%m.%Y %H:%M")
        return f"Оценка для {self.location.location_name} ({date_formatted})"

    class Meta:
        verbose_name_plural = "Оценки"