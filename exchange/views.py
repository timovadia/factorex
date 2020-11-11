# encoding: utf-8
from django.shortcuts import render
from django.template import Context
from django.http import Http404, HttpResponseRedirect
from exchange.models import Invoice
from customers.models import *
from customers.decorators import *
from django.contrib.auth import logout
from customers.forms import *
from accounts.models import *
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def land_page(request):
    delta0 = datetime.timedelta(minutes=5)
    delta1 = datetime.timedelta(hours=1)
    delta2 = datetime.timedelta(days=1, hours=1)
    delta3 = datetime.timedelta(days=1, hours=5)
    delta4 = datetime.timedelta(days=2, hours=1)
    delta5 = datetime.timedelta(days=2, hours=5)
    delta_modal = datetime.timedelta(days=50)
    time = datetime.datetime.now() - delta0
    time1 = time - delta1
    time2 = time - delta2
    time3 = time - delta3
    time4 = time - delta4
    time5 = time - delta5
    time6 = time - delta5 - delta1
    time_modal = time + delta_modal
    variables = Context({
        'time': time,
        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4,
        'time5': time5,
        'time6': time6,
        'time_modal': time_modal
    })
    return render(request, 'land_page.html', variables)

def index(request):
    user_role = 0
    if is_factor(request.user):
        user_role = 'factor'
    elif is_contractor(request.user):
        user_role = 'contractor'
    variables = Context({
        'user': request.user,
        'invoice_list': Invoice.objects.all(),
        'user_role': user_role
    })
    return render(request, 'index.html', variables)

def user_page(request, id):
    try:
        user = FexUser.objects.get(id=id)
    except FexUser.DoesNotExist:
        raise Http404(u'Requested user not found.')

    invoices = Invoice.objects.all()

    variables = Context({
        'id': id,
        'invoices': invoices
    })
    return render(request, 'user_page.html', variables)

@login_required
def account_page(request, id):
    try:
        user = FexUser.objects.get(id=id)
    except FexUser.DoesNotExist:
        raise Http404(u'Requested user not found.')

    variables = Context({
        'id': id
    })
    return render(request, 'account_page.html', variables)

def profile(request):
    if is_factor(request.user):
        return render(request, 'profile_factor.html',
                      {'company': request.user.factor_user.employer})
    elif is_contractor(request.user):
        return render(request, 'profile_contractor.html',
                      {'company': request.user.contractor_user.employer})
    raise Http404(u'Requested profile not found.')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_role = form.cleaned_data['user_role']
            user = FexUser.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            if user_role == 'f':
                FactorUser.objects.create(
                    employer=None,
                    user=user
                )
            elif user_role == 'c':
                ContractorUser.objects.create(
                    employer=None,
                    user=user
                )
            else:
                raise
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = Context({
        'form': form
    })
    return render(request, 'registration/register.html', variables)
