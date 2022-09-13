from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from requests import request
from myapp.models import QuoteTable
from django.urls import reverse_lazy
from myapp.forms import QuoteForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class QuoteHomeView(ListView):
    model=QuoteTable
    template_name='myapp/list.html'
    context_object_name='quotes'

class QuoteTagListView(QuoteHomeView):
    template_name='myapp/taglist.html'
    def get_tag(self):
        return self.kwargs.get('tag')
    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["tag"]=self.get_tag()
        return context
class QuoteDetailView(DetailView):
    model=QuoteTable
    template_name='myapp/detail.html'
    context_object_name='quotes'

# @method_decorator(login_required,name='form_valid')
class QuoteCreateView(LoginRequiredMixin,CreateView):
    model=QuoteTable
    fields=['quote','qauthor','qtype','qimage','tags']
    template_name='myapp/create.html'
    success_url=reverse_lazy('quotes:list')
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class UserIsSubmitter(UserPassesTestMixin):
    def get_quotes(self):
        return get_object_or_404(QuoteTable,pk=self.kwargs.get('pk'))
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user==self.get_quotes().username
        else:
            raise PermissionDenied('Sorry Your are not allowed to upload')
class QuoteUpdateView(UpdateView):
    
    model=QuoteTable
    # fields=['quote','qauthor','qtype','qimage','tags']
    fields='__all__'
    template_name='myapp/update.html'
    success_url=reverse_lazy('quotes:list')
class QuoteDeleteView(DeleteView):
    model=QuoteTable
    # template_name='myapp/delete.html'
    success_url=reverse_lazy('quotes:list')

















