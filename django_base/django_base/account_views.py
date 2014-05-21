from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from models import UserProfile
import person_attributes
from django.db import connection
import json
import datetime
import uuid

class UserCreationFromEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(
        label=('First name'),
        max_length=30,
        required=False)
    last_name = forms.CharField(
        label=('Last name'),
        max_length=30,
        required=False)

    class Meta:
        model = User
        fields = ( "username", "first_name", "last_name", "email" )

class BaseUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'country']

def profile(request):
    profile=request.user.get_profile()
    return render_to_response('accounts/profile.html', locals(), RequestContext(request))

def edit_profile(request):
    if request.method == 'POST':
        print "POST!"
        profile_form = BaseUserForm(request.POST, prefix='baseprofile', instance=request.user)
        extended_profile_form = ExtendedUserForm(request.POST,prefix='extendedprofile', instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save() 
        print extended_profile_form
        if extended_profile_form.is_valid():
            extended_profile_form.save() 
        return HttpResponseRedirect("/accounts/profile/")
    else:        
        profile_form = BaseUserForm(prefix='baseprofile', instance=request.user)
        extended_profile_form = ExtendedUserForm(prefix='extendedprofile', instance=request.user.userprofile)
        return render_to_response('accounts/edit_profile.html', locals(), RequestContext(request))

def register(request):
    if request.user.is_authenticated():
        return redirect('profile')

    if request.method == 'POST' and request.user.is_anonymous: 
        base_profile_form = UserCreationFromEmail(request.POST, prefix='baseprofile')
        extended_profile_form = ExtendedUserForm(request.POST,prefix='extendedprofile')

        if base_profile_form.is_valid():
            print "Base form is valid"
            username = base_profile_form.clean_username()
            password = base_profile_form.clean_password2()
            base_profile_form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)

            extended_profile_form = ExtendedUserForm(request.POST,prefix='extendedprofile', instance=request.user.userprofile)

            user.userprofile.save()

            if extended_profile_form.is_valid():
                print "Extended profile form valid"
                extended_profile_form.save()                  
            else:
                print "extended profile form not valid"
            return HttpResponseRedirect("/accounts/profile/")
        else:
            print "base form not valid"
    else:
        base_profile_form = UserCreationFromEmail(prefix='baseprofile')
        if request.user.is_anonymous:
            extended_profile_form = ExtendedUserForm(prefix='extendedprofile')
        elif request.user.userprofile:
            extended_profile_form = ExtendedUserForm(prefix='extendedprofile', instance=request.user.userprofile)



    return render_to_response('accounts/register.html', locals(), RequestContext(request))

