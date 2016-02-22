from __future__ import absolute_import

from django import template

from django.shortcuts import render

from ..forms import ChefForm
from ..shortcuts import render_template

register = template.Library()

@register.simple_tag(takes_context=True)
def chef_widget(context, meal, viewer):
    req = context['request']

    if meal.chef_id:
        # the chef herself!
        if viewer.id == meal.chef_id:
            # TODO: widget to vacate chef shift
            # meal requirements form
            form = ChefForm.for_meal(meal)

            return render_template(req, "meals/chef_requirements.html",
                {"form": form, "meal": meal})
        else:
            return render_template(req, "meals/chef_bio.html", {"meal": meal})

    else: # unclaimed chef shift
        # show chef signup form
        return render_template(req, "meals/chef_signup.html", {"meal": meal})

@register.simple_tag(takes_context=True)
def shift_widget(context, shift, user):
    # a claimed shift
    if shift.worker_id:
        # the worker
        if user.id == shift.worker_id:
            # TODO: widget to vacate shift
            return "quit the shift"
        else:
            # show worker
            return "working: %s" % user.username
    else:
        return "sign up for the shift"
