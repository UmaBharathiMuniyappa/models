from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
   # QLTO=Topic.objects.filter(topic_name__startswith='C')
   # QLTO=Topic.objects.filter(topic_name__endswith='l')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-topic_name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Cricket',name__endswith='l')
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name__endswith='i'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='V'))

    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().order_by('name')
    QLAO=AccessRecord.objects.all().order_by('author')
    QLAO=AccessRecord.objects.all().order_by('-name')
    QLAO=AccessRecord.objects.all().order_by('-author')
    QLAO=AccessRecord.objects.all().order_by(Length('name'))
    QLAO=AccessRecord.objects.all().order_by(Length('author'))
    QLAO=AccessRecord.objects.all().order_by(Length('name').desc())
    QLAO=AccessRecord.objects.all().order_by(Length('author').desc())
    #QLAO=AccessRecord.objects.filter(date__day__gt=11)
    QLAO=AccessRecord.objects.filter(author__contains='r')
    d={'accessrecords':QLAO}
    return render(request,'display_accessrecords.html',d)

def insert_topic(request):
    tn=input()
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return render(request,'display_topics.html')

def insert_webpage(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    return render(request,'display_webpages.html')

def insert_access(request):
    pk=int(input('enter pk for webpage'))
    a=input('enter author name')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return render(request,'display_accessrecords.html')

def update_webpage(request):
    QLWO=Webpage.objects.all()
    #Webpage.objects.filter(topic_name='Cricket').update(name='Virat Kohli')
    #Webpage.objects.filter(topic_name='BasketBall').update(name='James')
    #Webpage.objects.filter(topic_name='Kabaddi').update(name='Rohit Kumar')  #will not perform anything
    CTO=Topic.objects.get_or_create(topic_name='VolleyBall')[0]
    CTO.save()
    #Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'Balwant Singh'})
    
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)


def delete_access(request):
    QLAO=AccessRecord.objects.all()
    #AccessRecord.objects.filter(author='Virat').delete()
    AccessRecord.objects.all().delete()
    d={'accessrecords':QLAO}
    return render(request,'display_accessrecords.html',d)