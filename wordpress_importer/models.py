from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class PostImport(models.Model):
    post_id = models.IntegerField()
    article_page = models.ForeignKey("wagtailcore.Page", null=True)

    def __str__(self):
        return "{}".format(self.post_id)


@python_2_unicode_compatible
class ImageImport(models.Model):
    original_url = models.CharField(max_length=1024)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TagImport(models.Model):
    original_slug = models.CharField(max_length=1024)
    topic = models.ForeignKey("articles.Topic", null=True)

    def __str__(self):
        return "{} - {}".format(self.original_slug, self.topic.name)
