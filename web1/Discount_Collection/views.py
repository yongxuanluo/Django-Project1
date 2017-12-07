from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from  Discount_Collection.models import AccessRecord, UserProfileInfo
from  Discount_Collection.forms import NewUserForm, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return(render(request, 'Discount_Collection/index.html'))

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password) #hashing password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user #one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm() #if nothing, just set the form
        profile_form = UserProfileInfoForm()

    return render(request, 'Discount_Collection/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def table(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return(render(request, 'Discount_Collection/table.html', context = date_dict))

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Name: "+form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])


    return(render(request,'Discount_Collection/form_page.html',{'form':form}))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') #in login.html, the name of the username input is username
        password = request.POST.get('password')

        user = authenticate(username=username,password=password) #automatically authenticate the credential

        if user: #when pass authentication, equals TRUE
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index')) #if account is active and login successful, redirect to homepage
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Login Failed")
            return HttpResponse("Invalid Credential")
    else:
        return render(request, 'Discount_Collection/login.html',{})

@login_required #decorator must be a line above the function, this make sure you are logged in before log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def account_detail(request):
    return HttpResponse("Logged in")