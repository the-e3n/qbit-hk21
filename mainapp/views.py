from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from random import randrange
from .helpers.solution import solution

from mainapp import BING_API
from mainapp.helpers.mapApi import getMap

class Home(View):

    @staticmethod
    def get(request):
        context = {}
        request.session.clear()
        request.session.set_test_cookie()
        a = list()
        return render(request, 'index.html', context)

    @staticmethod
    def post(request):
        context = {}
        if not request.session.test_cookie_worked():
            return HttpResponse("<h1> Please Enable cookies First and Refresh</h1>")
        request.session['vanNumber'] = int(request.POST['vanNumber'])
        request.session['areaNumber'] = int(request.POST['areaNumber'])
        request.session['doseNumber'] = int(request.POST['doseNumber'])
        request.session['areas'] = [0] * request.session['areaNumber']
        request.session['doses'] = [0] * request.session['areaNumber']
        request.session['count'] = [0] * request.session['areaNumber']
        request.session['wastage'] = [0] * request.session['areaNumber']
        request.session['manual_data'] = bool(request.POST['manual_data']) if request.POST.get('manual_data') else False
        if request.session['manual_data']:
            return redirect('areaForm')
        for i in range(request.session['areaNumber']):
            request.session['areas'][i] = randrange(1, 200)
            request.session['doses'][i] = randrange(1, 10) * request.session['doseNumber']
        return redirect('final')


def areaForm(request):
    context = {}
    if request.method == 'POST':
        for i in range(request.session['areaNumber']):
            request.session['areas'][i] = int(request.POST[f'area{i}'])
            request.session.modified = True
        return redirect('doseForm')
    context['range'] = list(range(request.session['areaNumber']))
    return render(request, 'areaForm.html', context)


def doseForm(request):
    context ={}
    if request.method == 'POST':
        for i in range(request.session['areaNumber']):
            request.session['doses'][i] = int(request.POST[f'dose{i}']) * request.session['doseNumber']
            request.session.modified = True
        return redirect('final')
    context['range'] = list(range(request.session['areaNumber']))
    return render(request, 'doseForm.html', context)


class Final(View):
    @staticmethod
    def get(request):
        context = {}
        solution(request)
        # for i in range(request.session['areaNumber']):
        #     request.session['doses'][i] += randrange(0, 2) * request.session['doseNumber']
        print('Areas:-', request.session['areas'], 'Doses:-', request.session['doses'])
        context['range'] = list(range(request.session['areaNumber']))
        return render(request, 'final.html', context)

