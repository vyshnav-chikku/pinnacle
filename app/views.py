from django.shortcuts import render
from django.http import HttpResponseRedirect

from app.models import *

from app.forms import *
import hashlib
from django.contrib.auth import logout
import datetime

# Create your views here.
def home(request):
	return render(request,'home/index.html')

def jobfairhome(request):
	return render(request,'jobfair/index.html')

def employee_registration(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		phone=request.POST['phone']
		dob=request.POST['dob']
		age=request.POST['age']
		gender=request.POST['gender']
		marital_status=request.POST['marital_status']
		address=request.POST['address']
		language=request.POST['language']
		qalification=request.POST['qalification']
		experience=request.POST['experience']
		jobopted=request.POST['jobopted']
		compknowledge=request.POST['compknowledge']
		resume=request.FILES['resume']
		date = datetime.datetime.now().date()

		check=employee_tb.objects.all().filter(fname=fname,lname=lname,email=email,phone=phone,dob=dob,age=age,gender=gender,marital_status=marital_status,address=address,language=language,qalification=qalification,experience=experience,jobopted=jobopted,compknowledge=compknowledge,date=date)
		if check:
			return render(request,'home/employee.html',{'error':'Already Registerd '})
		else:
			add=employee_tb(fname=fname,lname=lname,email=email,phone=phone,dob=dob,age=age,gender=gender,marital_status=marital_status,address=address,language=language,qalification=qalification,experience=experience,jobopted=jobopted,compknowledge=compknowledge,resume=resume,date=date)
			add.save()
			return render(request,'home/employee.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'home/employee.html')






def employee_registration_jobfair(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		qualification=request.POST['qualification']
		experience=request.POST['experience']
		linkedin=request.POST['linkedin']
		category=request.POST['jobcategory']
		resume=request.FILES['resume']
		date = datetime.datetime.now().date()

		check=employee_tb_jobfair.objects.all().filter(name=name,email=email,phone=phone,qualification=qualification,experience=experience,linkedin=linkedin,category=category,date=date)
		if check:
			return render(request,'jobfair/employee.html',{'error':'Already Registerd '})
		else:
			add=employee_tb_jobfair(name=name,email=email,phone=phone,qualification=qualification,experience=experience,linkedin=linkedin,category=category,resume=resume,date=date)
			add.save()
			return render(request,'jobfair/employee.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'jobfair/employee.html')



def employer_registration(request):
	if request.method=="POST":
		logo = request.FILES['logo']
		nameorg = request.POST['nameorg']
		rname = request.POST['rname']
		email = request.POST['email']
		phone = request.POST['phone']
		phoner = request.POST['phoner']
		designation = request.POST['designation']
		website = request.POST['website']
		address = request.POST['address']
		job_file=request.FILES['job_file']
		date = datetime.datetime.now().date()

		# check=employer_tb.objects.all().filter(nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,positionnumber=positionnumber,gender=gender,jobtitle=jobtitle,description=description,positionnumber1=positionnumber1,gender1=gender1,jobtitle1=jobtitle1,description1=description1,positionnumber2=positionnumber2,gender2=gender2,jobtitle2=jobtitle2,description2=description2,positionnumber3=positionnumber3,gender3=gender3,jobtitle3=jobtitle3,description3=description3,positionnumber4=positionnumber4,gender4=gender4,jobtitle4=jobtitle4,description4=description4,date=date)
		check=employer_tb.objects.all().filter(nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,date=date)

		if check:
			return render(request,'home/employer.html',{'error':'Already Registerd '})
		else:
			add=employer_tb(logo=logo,nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,job_file=job_file,date=date)
			add.save()
		return render(request,'home/employer.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'home/employer.html')





def employer_registration_jobfair(request):
	if request.method=="POST":
		nameorg = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		rname = request.POST['rname']
		designation = request.POST['designation']
		website = request.POST['website']
		address = request.POST['address']
		job_file=request.FILES['file']
		date = datetime.datetime.now().date()

		# check=employer_tb.objects.all().filter(nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,positionnumber=positionnumber,gender=gender,jobtitle=jobtitle,description=description,positionnumber1=positionnumber1,gender1=gender1,jobtitle1=jobtitle1,description1=description1,positionnumber2=positionnumber2,gender2=gender2,jobtitle2=jobtitle2,description2=description2,positionnumber3=positionnumber3,gender3=gender3,jobtitle3=jobtitle3,description3=description3,positionnumber4=positionnumber4,gender4=gender4,jobtitle4=jobtitle4,description4=description4,date=date)
		check=employer_tb_jobfair.objects.all().filter(nameorg=nameorg,rname=rname,email=email,phone=phone,designation=designation,website=website,address=address,date=date)

		if check:
			return render(request,'jobfair/employer.html',{'error':'Already Registerd '})
		else:
			add=employer_tb_jobfair(nameorg=nameorg,rname=rname,email=email,phone=phone,designation=designation,website=website,address=address,job_file=job_file,date=date)
			add.save()
		return render(request,'jobfair/employer.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'jobfair/employer.html')





def admin_signup(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']		
		password=request.POST['password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		date = datetime.datetime.now().date()		
		check=admin_tb.objects.all().filter(email=email)
		if check:
			return render(request,"auth/signup.html",{'msgkey':"Mail id Already Registerd"})
			
		else:
			add=admin_tb(email=email,name=name,password=hashpass,pwd=password,date=date)
			add.save()
		return render(request,"auth/login.html")

	else:
		return render(request,'auth/signup.html')
	# return render(request,'pages-login.html')


def admin_login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		b=admin_tb.objects.all().filter(email=email,password=hashpass)
		if b.exists():
			for x in b:
				request.session["myid"]=x.id
				request.session["name"]=x.name

				return render(request,'auth/index.html')

		else:
			return render(request,'auth/login.html',{'msgkey':'Invalid credentials'})
	else:
		return render(request,'auth/login.html')
	


def logout(request):
    if request.session.has_key('myid'):
        del request.session['myid']
        del request.session['name']

        logout(request)
    return HttpResponseRedirect('/admin_login/')


def admin_index(request):
    if request.session.has_key('myid'):
        return render(request,'auth/index.html')
    return HttpResponseRedirect('/admin_login/')



def admin_view_employee(request):
    if request.session.has_key('myid'):
        query=employee_tb.objects.all()
        return render(request,'auth/employee_view.html',{'query':query})

    return HttpResponseRedirect('/admin_login/')


def admin_view_employer(request):
    if request.session.has_key('myid'):
        query=employer_tb.objects.all()
        return render(request,'auth/employer_view.html',{'query':query})
    return HttpResponseRedirect('/admin_login/')

def admin_view_employee_jobfair(request):
    if request.session.has_key('myid'):
        query=employee_tb_jobfair.objects.all()
        return render(request,'auth/pinnacle-employee.html',{'query':query})

    return HttpResponseRedirect('/admin_login/')

def admin_view_employer_jobfair(request):
    if request.session.has_key('myid'):
        query=employer_tb_jobfair.objects.all()
        return render(request,'auth/pinnacle-employer.html',{'query':query})

    return HttpResponseRedirect('/admin_login/')

########################################################################

def test(request):
	return render(request,'home/employer.html')
