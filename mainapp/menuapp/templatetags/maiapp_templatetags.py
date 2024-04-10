from django import template
from django.template.loader import render_to_string

from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    template_name = f'{menu_name}.html'
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render_to_string(template_name, {'menu_items': menu_items, 'request': context['request']})
