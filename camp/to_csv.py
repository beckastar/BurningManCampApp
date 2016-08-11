from cStringIO import StringIO
from unicodecsv import writer
from camp import models
from django.db.models import fields

User
    Vehicle
    Shelter
Meal
    MealShift


def local_fields(model):
    for f in model._meta.get_fields():
        if f.auto_created:
            continue

        if not f.is_relation:
            yield f
        elif f.related_model is not None:
            yield f

def dump_model(model):
    exists = model.objects.exists()
    return exists, model.objects.values()

def dump_models(models):
    for model in models:
        exists, rows = dump_model(model)
        if not exists:
            return []
        keys = None
        for row in rows:
            if keys is None:
                keys = sorted(row.keys())
            yield dump_row(keys, row)

def dump_row(keys, row):
    ret = []
    for key in keys:
        ret.append(row[key])
    return row