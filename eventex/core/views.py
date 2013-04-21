# coding: utf-8
from django.shortcuts import render

def homepage(request):
	return render(request, 'index.html')

'''
# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
	context = RequestContext(request)
	return render_to_response('index.html', context)
'''

'''
# coding: utf-8
from django.shortcuts import render_to_response
from django.conf import settings

def homepage(request):
	context = {'STATIC_URL': settings.STATIC_URL}
	return render_to_response('index.html', context)

'''

'''
# coding: utf-8
from django.shortcuts import render_to_response

def homepage(request):
	return render_to_response('index.html')
'''