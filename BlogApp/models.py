from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر")
    category = models.ForeignKey(Category, related_name="blog", verbose_name="دسته بندی", on_delete=models.CASCADE)
    category_slug = models.CharField(max_length=255, verbose_name="اسلاگ")
    author = models.CharField(max_length=255, verbose_name="نویسنده")
    date = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "وبلاگ"
        ordering = ("-date",)


class Full(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    introTitle = models.CharField(max_length=255, verbose_name="عنوان")
    author = models.CharField(max_length=255, verbose_name="عنوان توضیحات")
    content_desc = models.TextField(verbose_name="متن توضیحات")
    content_des2 = models.TextField(verbose_name="متن توضیحات", default=" ")

    class Meta:
        verbose_name = "توضیحات"
        verbose_name_plural = "توضیحات"


class Gallery(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری"
