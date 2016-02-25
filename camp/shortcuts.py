from django.conf import settings
from django.template import loader
from django.template import RequestContext, Context


def render_template(request, template, context=None):
    if not isinstance(template, list):
        template = [template]
    template = loader.select_template(template)
    return template.render(context or {}, request=request)

def get_current_event():
    from camp.models import Event

    if settings.CURRENT_EVENT_ID is None:
        return Event.objects.order_by('-start_date').first()
    else:
        return Event.objects.filter(pk=settings.CURRENT_EVENT_ID).get()
