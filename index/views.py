from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from  django.views.generic.base import View


class IndexView(View):
    """
    首页index
    """
    def get(self, request):
        return render(request, "index.html", )

class IndexView2(View):
    """
    首页index2
    """
    def get(self, request):
        return render(request, "result.html", )