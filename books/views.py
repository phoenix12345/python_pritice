from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render_to_response
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect


def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query)
            # Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response('search.html',{
        "results":results,
        "query":query
    })

@csrf_protect
def contact(request):
    if request.method == 'post':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender','lanzechuan@sinosoft.com.cn')
            send_mail(
                'Feedback from your site,topic:%s'%topic,
                message,sender,
                ['lanzechuan@sinosoft.com.cn']
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
