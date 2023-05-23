from django.db import models
from django.utils import timezone
from django.urls import reverse
from colorful.fields import RGBColorField

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField('Местоположение', max_length=50)
    location_link = models.CharField('Ссылка на страницу', max_length=200, blank=True, null=True, editable=False)
    location_header = models.CharField('Заголовок', max_length=100, null=True)
    location_header_fs = models.IntegerField(default=30)
    header_color = RGBColorField('Цвет текста', null=True)
    main_image = models.ImageField(upload_to='location_images/', null=True)
    like_image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    dislike_image = models.ImageField(upload_to='location_images/', blank=True, null=True)

    def __str__(self):
        return self.location_name
    def save(self, *args, **kwargs):
        if not self.location_link:
            self.location_link = reverse('ratings:location_rating', args=[self.location_name])
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

class Rating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField()
    dislike = models.BooleanField()

    def __str__(self):
        date_formatted = self.date_created.strftime("%d.%m.%Y %H:%M")
        result_formatted = "Лайк" if self.like else "Дизлайк"
        return f"{result_formatted} {date_formatted}"
        #return f"Оценка {self.location.location_name} ({date_formatted})"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"