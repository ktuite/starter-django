from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
    print "trying to render this index thing"
    my_variable = "cats"
    return render_to_response('custom_app/index.html', locals(), RequestContext(request))

def simple_view(request):
    return HttpResponse('Here is some text on a webpage!')