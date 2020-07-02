from django.db import models

class TopicModel(models.Model) :
    topic_idx = models.AutoField(primary_key=True)
    topic_name = models.TextField(null=False)

class ContentModel(models.Model) :
    content_idx = models.AutoField(primary_key=True)
    content_topic_idx = models.ForeignKey(TopicModel, null=False, on_delete=models.CASCADE)
    content_text = models.TextField(null=False)