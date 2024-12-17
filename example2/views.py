from django.shortcuts import render
from django.views.generic import TempLateView
# Create your views here.

def index(request):
  return render(request, 'class_template.html')

class index2(TempLateView):
  template_name = "func_template.html"
