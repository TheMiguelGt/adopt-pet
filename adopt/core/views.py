from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,{'title':'Home'})
    