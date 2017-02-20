from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Clipboard

class IndexView(generic.ListView):
    template_name = 'pastebin/index.html'
    context_object_name = 'pasted_list'

    def get_queryset(self):
        return Clipboard.objects.order_by('-create_date').all()

def submit(request):
    paste_text=request.POST['paste_text']
    create_date=timezone.now()
    new = Clipboard(paste_text=paste_text,create_date=create_date)
    new.save()
    return HttpResponseRedirect('.')
