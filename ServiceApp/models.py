from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    preview_title = models.CharField(max_length=255, verbose_name="عنوان پیش نمایش")
    short = models.CharField(max_length=255, verbose_name="توضیح کوتاه")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"


class Full(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    introTitle = models.CharField(max_length=255, verbose_name="عنوان")
    title_desc = models.CharField(max_length=255, verbose_name="عنوان توضیحات")
    content_desc = models.TextField(verbose_name="متن توضیحات")

    class Meta:
        verbose_name = "توضیحات"
        verbose_name_plural = "توضیحات"


class List(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="list")
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.TextField(verbose_name="مقدار")


class Process(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن توضیحات")
    number = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "روند"
        verbose_name_plural = "روند ما"

