from django.views.generic import FormView
from .forms import ContactsUsModelForm

class ContactUsView(FormView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactsUsModelForm
    success_url = 'home'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)