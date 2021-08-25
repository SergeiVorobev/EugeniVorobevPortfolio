from django.shortcuts import render
from portfolio.models import MyApp
from portfolio.models import Certificate
from django.core.mail import send_mail


# from .models import Contact
from django.http import HttpResponse

# Create your views here.
def home(request):

    all_apps = MyApp.objects.all()
    all_cert = Certificate.objects.all()

    context = {
        'my_apps': all_apps,
        'certificates': all_cert,
    }

    if request.method == "POST":
        m_name = request.POST['name']
        m_email = request.POST['email']
        m_phone = request.POST["phone"]
        m_message = request.POST["message"]
        # context['name'] = m_name
        # context['message2'] = 'Я скоро свяжусь с Вами'


        # send an email
        send_mail(
            m_name + ' with phone ' + m_phone, # subject
            m_message, # message
            # m_phone, # from email
            m_email, # from email
            ['evorob4@mail.ru'],# to email
        )
        # cont.name = name
        # cont.email = email
        # cont.phone = phone
        # cont.message = message
        # cont.save()
        # return HttpResponse("<h1>Ваше письмо было успешно отправлено</h1>")
    #     return render(request, 'website/index.html', context)
    # else:
    #     return render(request, 'website/index.html', context)

    return render(request, 'website/index.html', context)

