from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200 , verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    image = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر")
    category = models.ManyToManyField(Category, related_name="project", verbose_name="دسته بندی")
    date = models.CharField(max_length=25, verbose_name="تاریخ پروژه")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class Full(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    introTitle = models.CharField(max_length=255, verbose_name="عنوان")
    fullImage = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر بزرگ")
    title_desc = models.CharField(max_length=255, verbose_name="عنوان توضیحات")
    content_desc = models.TextField(verbose_name="متن توضیحات")

    class Meta:
        verbose_name = "توضیحات"
        verbose_name_plural = "توضیحات"


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="Detail")
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "جزئیات"
        verbose_name_plural = "جزئیات"


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری"


class Gallery2(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery2")
    image = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری دوم"
