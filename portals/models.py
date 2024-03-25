from django.db import models
import uuid


# Create your models here.

class BaseModel(models.Model):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_on",)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        return ret
