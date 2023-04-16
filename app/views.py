from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic_name']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic data is inserted successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage data is inserted Successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LOA=Webpage.objects.all() 
    d={'access':LOA}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)
        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('<h1>Accessrecord data is inserted successfully</h1>')
    return render(request,'insert_access.html',d)
