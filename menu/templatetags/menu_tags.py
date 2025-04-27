from django import template
from django.urls import reverse, NoReverseMatch
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').order_by('order')

    def build_tree(items, parent_id=None):
        result = []
        for item in items:
            if item.parent_id == parent_id:
                try:
                    url = reverse(item.named_url) if item.named_url else item.url
                except NoReverseMatch:
                    url = item.url or '#'

                is_active = current_path == url
                children = build_tree(items, item.id)

                # Проверяем активность детей для автоматического раскрытия
                has_active_child = any(child['is_active'] or child['has_active_child'] for child in children)

                node = {
                    'item': item,
                    'url': url,
                    'is_active': is_active,
                    'children': children,
                    'has_active_child': has_active_child,
                    'should_expand': is_active or has_active_child
                }
                result.append(node)
        return result

    return {
        'menu_tree': build_tree(items),
        'current_path': current_path
    }