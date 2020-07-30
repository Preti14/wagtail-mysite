from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    """ Home page models    """
    templates = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle = RichTextField(features=["bold","italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [FieldPanel("banner_title")]

    class Meta:
        verbose_name = "Single Home 1"
        verbose_name_plural = "Multiple Home"