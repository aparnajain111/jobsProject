from django.shortcuts import render
from jobsapp.models import hydjobs,punejobs,chennaijobs,blorjobs
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def homePage(request):
    return render(request=request,template_name='jobsapp/home.html')

def hydjobsinfo(request):
    hyd_list = hydjobs.objects.order_by('date')
    paginator = Paginator(hyd_list,5)
    page_number = request.GET.get('page')
    try:
        hyd_list = paginator.page(page_number)
    except PageNotAnInteger:
        hyd_list = paginator.page(1)
    except EmptyPage:
        hyd_list = paginator.page(paginator.num_pages)
    my_dict = {'hyd_list':hyd_list}
    return render(request=request,template_name='jobsapp/hydjobs.html',context=my_dict)

def punejobsinfo(request):
    pune_list = punejobs.objects.order_by('date')
    my_dict = {'pune_list':pune_list}
    return render(request=request,template_name='jobsapp/punejobs.html',context=my_dict)  

def chennaijobsinfo(request):
    chennai_list = chennaijobs.objects.order_by('date')
    my_dict = {'chennai_list':chennai_list}
    return render(request=request,template_name='jobsapp/chjobs.html',context=my_dict)

def blorjobsinfo(request):
    blor_list = blorjobs.objects.order_by('date')
    my_dict = {'blor_list':blor_list}
    return render(request=request,template_name='jobsapp/blorjobs.html',context=my_dict)          