import uuid

from django.db import models


class Entity(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=False, db_column='created_at')
    updated = models.DateTimeField(auto_now=True, null=False, db_column='updated_at')
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     editable=False, default=settings.AUTH_USER_MODEL
    # )


class Manufactures(Entity):
    ManufactureName = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)

    def __str__(self):
        return self.ManufactureName
