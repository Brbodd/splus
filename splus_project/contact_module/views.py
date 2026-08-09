from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ContactsUsModelForm

def contact_us_page(request):
    contact_form = ContactsUsModelForm(request.POST or None)
    
    if request.method == 'POST' and contact_form.is_valid():
        contact_form.save()
        return redirect('home')

    return render(request, 'contact_module/contact_us.html', {
        'contact_form': contact_form
    })

class ContactUsView(FormView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactsUsModelForm
    success_url = 'home'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)