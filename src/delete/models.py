from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models


class PostManager(models.Manager):
    def all(self):
        qs = super(PostManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(PostManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs

class deletePost(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent      = models.ForeignKey("self", null=True, blank=True)

    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta:
        ordering = ['-timestamp']


    def get_delete_url(self):
        return reverse("deletePost:delete", kwargs={"id": self.id})
        
    

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True



