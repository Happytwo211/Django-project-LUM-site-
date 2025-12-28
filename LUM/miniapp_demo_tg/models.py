from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.db import models


class Tour(models.Model):
    tour_name = models.CharField(max_length=50, verbose_name='Название экскурсии')
    tour_description = models.TextField(
        verbose_name='Описание экскурсии',
        validators=[MinLengthValidator(10, message='Минимальная длина описания - 10 символов')]
    )
    tour_img = models.ImageField(upload_to='tours_media/tours_img', null=True, blank=True)
    tour_content_type = models.CharField(default='Экскурсия', editable=False, max_length=10)
    tour_created_time = models.TimeField(auto_now=True, verbose_name='Время создания')
    tour_created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_tour_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'
        ordering = ['-tour_created_date']

    def __str__(self):
        return f'{self.tour_name} : {self.tour_created_date}'

class TourDropDownElements(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='drop_down_elements',
        verbose_name='Элементы экскурсии'
    )
    element_name = models.CharField(max_length=100, verbose_name='Название элемента экскурсии')
    element_description = models.TextField(verbose_name='Описание элемента экскурсии', blank=True)
    element_icon = models.ImageField(upload_to='tour_el_media/icons', blank=True, null=True)
    element_created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания элемента экскурсии')
    element_img = models.ImageField(upload_to='tour_el_media/photo', verbose_name='Фото', blank=True, null=True)
    element_video = models.FileField(
        upload_to='tour_el_media/video',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])],
        verbose_name='Видео',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Элемент выпадающего списка'
        verbose_name_plural = 'Элементы выпадающего списка'
        ordering = ['element_created_at', 'element_name']

    def __str__(self):
        return f'{self.tour} : {self.element_name}, {self.element_created_at}'

class TG_Profile(AbstractBaseUser):
    tg_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=64, default='user_name', null=False)
    second_name = models.CharField(max_length=64, null=True)
    user_icon = models.URLField(max_length=500, blank=True, null=True)