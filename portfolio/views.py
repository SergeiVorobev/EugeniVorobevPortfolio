from django.shortcuts import render
from portfolio.models import MyApp
from portfolio.models import Certificate



# Create your views here.
def home(request):
    # name = "John"
    all_apps = MyApp.objects.all()
    all_cert = Certificate.objects.all()

    context = {
        'my_apps': all_apps,
        'certificates': all_cert,
    }

    return render(request, 'website/index.html', context)
