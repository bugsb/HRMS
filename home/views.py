from django.shortcuts import render, redirect, HttpResponse
from .models import *

from .services import *


def view(request, type, id):
    if type == 'GM':
        data = Service.get_GM_data(id)
        return render(request, 'view.html', data)

    elif type == 'RGM':
        data = Service.get_RGM_data(id)
        return render(request, 'view.html', data)

    elif type == 'AGM':
        data = Service.get_AGM_data(id)
        return render(request, 'view.html', data)


def add_sales(request, type, id):
    if type == "RGM":  # Added by GM
        Service.update_GM_sales(id)
        return redirect(request.META['HTTP_REFERER'])

    elif type == "AGM":  # Added by RGM
        Service.update_RGM_sales(id)
        return redirect(request.META['HTTP_REFERER'])

    elif type == "DM":  # Added by AGM
        Service.update_AGM_sales(id)
        return redirect(request.META['HTTP_REFERER'])


def remove_sales(request, type, id):
    if type == "RGM":
        Service.decrease_GM_sales(id)
        return redirect(request.META['HTTP_REFERER'])

    elif type == "AGM":
        Service.decrease_RGM_sales(id)
        return redirect(request.META['HTTP_REFERER'])
    elif type == "DM":
        Service.decrease_AGM_sales(id)
        return redirect(request.META['HTTP_REFERER'])


def view_rgms(request):

    list_ = RGM.objects.all()
    data = {'list': list_, 'type': 'RGM'}
    return render(request, 'list.html', data)


def view_gms(request):
    list_ = GM.objects.all()
    data = {'list': list_, 'type': 'GM'}
    return render(request, 'list.html', data)


def view_agms(request):
    list_ = AGM.objects.all()
    data = {'list': list_, 'type': 'AGM'}
    return render(request, 'list.html', data)


def view_dms(request):
    list_ = DM.objects.all()
    data = {'list': list_, 'type': 'DM'}
    return render(request, 'list.html', data)


def form(request, type, id):
    data = {'id': id, 'type': type}
    return render(request, 'form.html', data)


def submit(request, type, fk):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        if type == 'RGM':
            Service.add_new_RGM(name,email,fk)
            return redirect('/view_rgms')
        elif type == 'AGM':
            Service.add_new_AGM(name,email,fk)
            return redirect('/view_agms')
        elif type == 'DM':
            Service.add_new_DM(name,email,fk)
            return redirect('/view_dms')
    else:
        return HttpResponse('Method Not Allowed')
