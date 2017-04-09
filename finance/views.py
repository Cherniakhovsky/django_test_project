from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def base(request):
    #return HttpResponse("This is a start page of my practice_project")
	context_dict={'mess':"Life is good :-)"}
	return render(request, 'finance/base.html', context_dict)


def about(request):
	return HttpResponse("About the Finance project")