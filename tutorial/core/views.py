from django.template.loader import render_to_string
from django.http import HttpResponse




# Create your views here.
def index(request):
    html = render_to_string('profile.html',
    { 
        'name': 'Veerawat Prodpran',
        'nick_name': 'Wat',
        'birth_date': '11/08/1993',
        'email': 'veerawat@odds.team',
        'tel': '0000000000',
    }
    )
    return HttpResponse(html)
