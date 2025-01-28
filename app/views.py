from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_Topic_fe(request):
     if request.method=='POST':
       topic_name=request.POST["topic_name"]
       TTO=Topic.objects.get_or_create(topic_name=topic_name)
       if TTO[1]:
            return HttpResponse(f'{topic_name} object is created')
       else:
            return HttpResponse(f'{topic_name} object is already present')
   
     return render(request,'insert_Topic_fe.html')


def insert_webpage_fe(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
     tn=request.POST["tn"]
     na=request.POST["na"]
     ur=request.POST['ur']
     em=request.POST['em']
     TO=Topic.objects.get(topic_name=tn)
     TWO=Webpages.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)
     if TWO[1]:
         return HttpResponse(f'{na} is created')
     else:
         return HttpResponse(f'{na} is already present')
    return render(request,'insert_webpage_fe.html',d)

def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        ltns=request.POST.getlist('tns')
        WEQS=Webpages.objects.none()
        for tn in ltns:
            WEQS=WEQS|Webpages.objects.filter(topic_name=tn)
            d1={'LWO':WEQS}
        return render(request,'display_webpages.html',d1)

    return render(request,'select_multiple.html',d)

def select_checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    # if request.method=='POST':
    #     ltns=request.POST.getlist('tns')
    #     WEQS==Webpages.objects.none()
    #     for tn in ltns:
    #         WEQS=WEQS|Webpages.objects.filter(topic_name=tn)
    #         d1={'LWO':WEQS}
    #     return render(request,'display_webpages.html',d1)

    return render(request,'select_checkbox.html',d)