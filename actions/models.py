from django.conf import settings
from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Action(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 related_name='actions',
							 db_index=True,
							 on_delete=models.CASCADE)
	verb = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType, 
								     on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	target = GenericForeignKey('content_type', 'object_id')

	class Meta:
		ordering = ('-created',)
			
