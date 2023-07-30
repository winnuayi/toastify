from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'company/index.html',{
            'home_active': 'n-active'
        })


class MenuView(View):
    def get(self, request):
        return render(request, 'company/menu.html', {
            'menu_active': 'n-active'
        })


class AboutUsView(View):
    def get(self, request):
        return render(request, 'company/about-us.html', {
            'aboutus_active': 'n-active'
        })