from django.shortcuts import render,redirect 
from myapp.form import EmployeeForm
  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})    

from django.shortcuts import render  
from django.http import HttpResponse  
  
def setsession(request):  
    request.session['sname'] = 'Yogesh'  
    request.session['semail'] = 'yhraje@gmail.com'  
    
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    
    return HttpResponse(studentname+" "+studentemail );  


from django.shortcuts import render  
from django.http import HttpResponse  
  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('EdunetFoundation', 'Bengaluru')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['EdunetFoundation']  
    return HttpResponse(tutorial);  


from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
def index(request):  
    return render(request,'index.html')   