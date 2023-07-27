from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def setcookies(request):
 response=render(request,'mycookie/setcookies.html')
  #response has response object 
 #response.set_cookie('name','sonam',max_age=180)
 response.set_cookie('lname','sonami',expires=datetime.utcnow()+timedelta(days=2))
 return response

def getcookies(request):
# nm= request.COOKIES['name']
 nm=request.COOKIES.get('name',"Guest")
 return render(request,'mycookie/getcookies.html',{'name':nm})

def deletecookies(request):
   response=render(request,'mycookie/delcookies.html')
   response.delete_cookie('name')
   return response
  