from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name   = "top.html"

top     = TopView.as_view()

class ProductListView(LoginRequiredMixin,ListView):
    model           = Product   
    #template_nameを利用することでtemplateの名前を変更できる
    #template_name   = "crud/list.html"
    
    #ページネーションの設定
    paginate_by     = 3 #3個ごとにページを切り替える

lists   = ProductListView.as_view()

class ProductCreateView(LoginRequiredMixin,CreateView):
    model   = Product
    fields  = '__all__'

create  = ProductCreateView.as_view()

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model                   = Product
    fields                  = '__all__'
    template_name_suffix    = '_update_form'
    
edit    = ProductUpdateView.as_view()

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model                   = Product
    success_url             = reverse_lazy('crud:list')
    
delete  = ProductDeleteView.as_view()

class ProductDetailView(LoginRequiredMixin,DetailView):
    model   = Product

detail = ProductDetailView.as_view()

class LoginView(LoginView):
    form_class      = AuthenticationForm
    template_name   = 'crud/login.html'
    
login   = LoginView.as_view()

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name   = 'crud/top.html' 

logout  = LogoutView.as_view()