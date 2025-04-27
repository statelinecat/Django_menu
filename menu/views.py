from django.views.generic import TemplateView

class BaseView(TemplateView):
    """Базовый класс для всех представлений"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class IndexView(BaseView):
    template_name = 'index.html'

class AboutView(BaseView):
    template_name = 'about.html'

class TeamView(BaseView):
    template_name = 'team.html'

class ContactView(BaseView):
    template_name = 'contact.html'

class CatalogView(BaseView):
    template_name = 'catalog.html'

class ProductCategoryView(BaseView):
    category_name = None
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.category_name
        return context

class AttackersView(ProductCategoryView):
    category_name = 'Нападающие'
    template_name = 'attackers.html'

class DefendersView(ProductCategoryView):
    category_name = 'Защитники'
    template_name = 'defenders.html'

class SkatesView(ProductCategoryView):
    category_name = 'Коньки'
    template_name = 'skates.html'

class ClubsView(ProductCategoryView):
    category_name = 'Клюшки'
    template_name = 'clubs.html'