from django import template
from main.models import Menu

register = template.Library()

@register.inclusion_tag('main/tree_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name, parent_menu=None)
    menu_context = {'menu_item': menu}
    menu_url = context['request'].path
    try:
        now_menu = Menu.objects.get(url_menu=menu_url)
    except:
        pass
    else:
        open_menu = now_menu.get_tree() + [now_menu.id]
        menu_context['open_menu'] = open_menu
    return menu_context

@register.inclusion_tag('main/tree_menu.html', takes_context=True)
def draw_menu_children(context, menu_item_id):
    menu_item = Menu.objects.get(pk=menu_item_id)
    children_context = {'menu_item': menu_item}
    if 'open_menu' in context:
        children_context['open_menu'] = context['open_menu']
    return children_context
