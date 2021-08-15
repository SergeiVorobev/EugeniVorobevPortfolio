from django.shortcuts import render
from portfolio.models import MyApp
from portfolio.models import Certificate
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def home(request):

    if request.method=="POST":
        cont = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        cont.name = name
        cont.email = email
        cont.phone = phone
        cont.message = message
        cont.save()
        # return HttpResponse("<h1>Ваше письмо было успешно отправлено</h1>")
        return render(request, 'website/index.html', {'name': name})
    else:
        return render(request, 'website/index.html', {})

    all_apps = MyApp.objects.all()
    all_cert = Certificate.objects.all()

    context = {
        'my_apps': all_apps,
        'certificates': all_cert,
    }

    return render(request, 'website/index.html', context)

