from django.db      import models
from core.models    import TimeStampModel

class User(TimeStampModel):
    email      = models.EmailField(max_length=45, unique=True)
    name       = models.CharField(max_length=45)
    nickname   = models.CharField(max_length=45)
    kakao_id   = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'