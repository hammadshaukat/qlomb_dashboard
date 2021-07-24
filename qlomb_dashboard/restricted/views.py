from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from qlomb_dashboard.users.models import User
from django.views.generic import TemplateView


class RestrictedView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'restricted.can_access_restricted_view'
    template_name = "restricted/restricted_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
