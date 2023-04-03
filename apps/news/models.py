from django.db import models
from ckeditor.fields import RichTextField


# News model
class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.CharField("affiliation", max_length=100, blank=True, null=True)
    external_link = models.URLField('external link', blank=True, null=True)
    published_date = models.DateTimeField("date published", auto_now=False, auto_now_add=False)  # published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news, not show in the webpage
    news_content = RichTextField(blank=True, null=True)
    cover_img = models.ImageField("cover image", upload_to='news/')
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "news"  # name in the admin site
        verbose_name_plural = verbose_name