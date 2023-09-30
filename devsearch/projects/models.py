from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    # Owner field
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # Featured Image
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_code = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
