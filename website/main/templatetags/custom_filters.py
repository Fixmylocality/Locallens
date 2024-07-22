# main/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """Splits a string by the given delimiter and returns a list of values."""
    return value.split(delimiter)
