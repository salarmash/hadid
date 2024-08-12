from django.db import models


class Team(models.Model):
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    role = models.CharField(max_length=255, verbose_name="موقعیت شغلی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "عضو"
        verbose_name_plural = "اعضای تیم"


class Social(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="social")
    link = models.CharField(max_length=255, verbose_name="لینک")
    icon = models.ImageField(upload_to="Icon", blank=True, null=True, verbose_name="آیکون")
    title = models.CharField(max_length=255, verbose_name="نام شبکه اجتماعی")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"
