from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    ## Foreign Key that looks for users who can post - Link to another
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ## Setup Basic Fields, Character Field for Title, Text for Blog Post, Dates for Stamps
    title = models.CharField(max_length=200) ## Short Text Field with limits
    text = models.TextField() ## Long Text Field without limits
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        ## When called set the new published date to the current time and save to DB
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        ## When called give a definition of the model, in example title of the post
        return self.title