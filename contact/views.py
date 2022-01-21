from django.shortcuts import redirect, render
from mainapp.models import *

# Create your views here.
from .forms import *

def contact(request):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    adds_contact = AddsContact.objects.all()
    contact_info = ContactInfo.objects.all()
    our_branch = OurBranch.objects.all()

    form = ContactUserForm()
    if request.method == 'POST':
        form = ContactUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactUserForm()

    context = {
        'mainCategory':mainCategory,
        'last_three':last_three,
        'form':form,
        'adds_contact':adds_contact,
        'contact_info':contact_info,
        'our_branch':our_branch,
    }
    return render(request, 'contact.html', context)
