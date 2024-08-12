from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادکی")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن درخواست")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"
