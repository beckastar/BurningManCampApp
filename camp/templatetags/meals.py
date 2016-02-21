from django import template

register = template.Library()

@register.filter
def chef_widget(meal, viewer):
    if meal.chef_id:
        # the chef herself!
        if viewer.id == chef.camper_id:
            # TODO: widget to vacate chef shift
            "quit as chef"
        else:
            # meal requirements form
            return "shift requirements?"
    else: # unclaimed chef shift
        # show chef signup form
        return "sign up as chef"

@register.filter
def shift_widget(shift, user):
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
