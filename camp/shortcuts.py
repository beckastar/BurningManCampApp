from django.template import loader
from django.template import RequestContext, Context


def render_template(request, template, context=None):
    if not isinstance(template, list):
        template = [template]
    template = loader.select_template(template)
    return template.render(context or {}, request=request)
