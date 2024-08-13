from django.db import models


class Hero(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    description = models.TextField(verbose_name="زیرنوشت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "هدر سایت"
        verbose_name_plural = "هدر سایت"


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="تصویر")
    icon = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="آیکون")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = " درباره ما"


class Service(models.Model):
    title1 = models.CharField(max_length=255, verbose_name="عنوان")
    title2 = models.CharField(max_length=255, verbose_name="زیر عنوان")
    subtitle = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "خدمات"


class ServiceItems(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="serviceItems")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.CharField(max_length=255, verbose_name="زیر عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتمها"


class Testimonial(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.TextField(verbose_name="زیرنوشت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشتریان"
        verbose_name_plural = "مشتریان"


class TestItems(models.Model):
    test = models.ForeignKey(Testimonial, on_delete=models.CASCADE, related_name="tetsItems")
    name = models.CharField(max_length=255, verbose_name="نام")
    role = models.CharField(max_length=255, verbose_name="شغل")
    text = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتمها"


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام شرکت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="لوگو")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "همکار"
        verbose_name_plural = "همکاران"

