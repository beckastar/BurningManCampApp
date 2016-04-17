from __future__ import absolute_import


from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


register = template.Library()

@register.simple_tag
def image(img):
    if not (img and img.url):
        return make_safe('No photo available.')
    else:
        return mark_safe(
            "<img src='%s'>" % conditional_escape(img.url))
