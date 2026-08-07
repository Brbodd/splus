from django.shortcuts import render, redirect
from .forms import ContactsUsModelForm

def contact_us_page(request):
    contact_form = ContactsUsModelForm(request.POST or None)
    
    if request.method == 'POST' and contact_form.is_valid():
        contact_form.save()
        return redirect('home')

    return render(request, 'contact_module/contact_us.html', {
        'contact_form': contact_form
    })
