from datetime import datetime
from msilib import datasizemask
from zoneinfo import ZoneInfo
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from todo.models import Weight, Running
from todo.forms import CreateForm, AddWeightForm, RunningForm

def home(response):
    return render(response, "todo/home.html", {})

def running(response):
    response = HttpResponse()
    response.write("<body><html>\n")
    response.write("<title>Running away!</title>\n")
    wlist = Running.objects.all()
    for p in reversed(wlist):
        central = p.timeenter.astimezone(ZoneInfo("US/Central"))
        ye = central.year
        mo = central.month
        da = central.day
#        wdate = "%s-%s-%s" % (ye,mo,da)  # YYYY-MM-DD
        wdate = "%s/%s/%s" % (mo,da,ye)   # MM/DD/YYYY
        junk = "I ran %s minutes on %s" % (p.minutes,wdate)
        response.write("%s -> %s<br>" % (junk,p.data))
    response.write("that is all, folks")
    response.write("</body></html>")
    return response

def addweight(response):
    if response.method == "POST":
        form = AddWeightForm(response.POST)
        l = Weight.objects.last()
        lastentry = l.timeenter.day
        t = datetime.now()
        today = t.day
        debug = str(lastentry) + " " + str(today) + " !! "
        print (debug)
        if lastentry == today:
            form = AddWeightForm()
        else:
            if form.is_valid():
                d = form.cleaned_data["data"]
                w = form.cleaned_data["damage"]  # 'damage' == cutesy name for weight
                f = Weight(data=d, damage=w)
                f.timeenter = datetime.now()
                f.save()
                form = AddWeightForm()
    else:
        form = AddWeightForm()
    return render(response, "todo/addweight.html", {"form": form})

def logweight(response):
    response = HttpResponse()
    response.write("<body><html>\n")
    response.write("<title>add todays weight into the database</title>\n")
    wlist = Weight.objects.all()
    for p in reversed(wlist):
        central = p.timeenter.astimezone(ZoneInfo("US/Central"))
        ye = central.year
        mo = central.month
        da = central.day
        wdate = "%s-%s-%s" % (ye,mo,da)  # YYYY-MM-DD
#        wdate = "%s/%s/%s" % (mo,da,ye)   # MM/DD/YYYY
#        junk = "I weighed %s on %s" % (p.damage,central)
        junk = "I weighed %s on %s" % (p.damage,wdate)
        response.write("%s -> %s<br>" % (junk,p.data))
    response.write("that is all, folks")
    response.write("</body></html>")
    return response

def addrun(response):
    if response.method == "POST":
        form = RunningForm(response.POST)
        if form.is_valid():
            d = form.cleaned_data["data"]    
            m = form.cleaned_data["minutes"]
            f = Running(data=d, minutes=m)
            f.timeenter = datetime.now()
            f.save()
            form = RunningForm()
    else:
        form = RunningForm()
    return render(response, "todo/addrun.html", {"form": form})
