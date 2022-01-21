from django.shortcuts import render
from mainapp.models import *
# Create your views here.
from .models import (
    OurTeam,
    Adds_News,
    BrandImage,
    Brends
)

def about(request):
    centerBrand = Brends.objects.all()
    brand_icons = BrandImage.objects.all()
    add_new = Adds_News.objects.all()
    team_member = OurTeam.objects.all().order_by('-date_modified')
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()


    context = {
        'centerBrand':centerBrand,
        'brand_icons':brand_icons,
        'team_member':team_member,
        'add_new':add_new,
        'mainCategory':mainCategory,
        'last_three':last_three,
    }
    return render(request, 'about.html', context)
