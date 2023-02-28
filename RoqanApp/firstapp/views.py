from django.http import HttpResponse
from django.template import loader
from .models import Customer


def MyCustomer(request):
    services = Customer.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'services': services,
    }
    return HttpResponse(template.render(context, request))
