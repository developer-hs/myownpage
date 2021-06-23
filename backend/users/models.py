from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    RESIDENCE_Seoul = "1835848"
    RESIDENCE_Incheon = "1843561"
    RESIDENCE_Gangwon = "1843125"
    RESIDENCE_Gyeonggi = "1841610"
    RESIDENCE_Busan = "1838524"
    RESIDENCE_Ulsan = "1833742"
    RESIDENCE_Gyeongsangnam = "1902028"
    RESIDENCE_Daegu = "1835327"
    RESIDENCE_Gyeongsangbuk = "1841597"
    RESIDENCE_Daejeon = "1835224"
    RESIDENCE_Chungcheongnam = "1845105"
    RESIDENCE_Chungcheongbuk = "1845106"
    RESIDENCE_Gwangju = "1841808"
    RESIDENCE_Jeollanam = "1845788"
    RESIDENCE_Jeollabuk = "1845789"
    RESIDENCE_Jeju = "1846265"

    RESIDENCE_CHOICES = (
        (RESIDENCE_Seoul, _("서울")),
        (RESIDENCE_Incheon, _("인천")),
        (RESIDENCE_Gangwon, _("강원도")),
        (RESIDENCE_Gyeonggi, _("경기도")),
        (RESIDENCE_Busan, _("부산")),
        (RESIDENCE_Ulsan, _("울산")),
        (RESIDENCE_Gyeongsangnam, _("경상남도")),
        (RESIDENCE_Daegu, _("대구")),
        (RESIDENCE_Gyeongsangbuk, _("경상북도")),
        (RESIDENCE_Daejeon, _("대전")),
        (RESIDENCE_Chungcheongnam, _("충청남도")),
        (RESIDENCE_Chungcheongbuk, _("충청북도")),
        (RESIDENCE_Gwangju, _("광주")),
        (RESIDENCE_Jeollanam, _("전라남도")),
        (RESIDENCE_Jeollabuk, _("전라북도")),
        (RESIDENCE_Jeju, _("제주도")),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    residence = models.CharField(
        _("residence"), choices=RESIDENCE_CHOICES, max_length=30)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email
