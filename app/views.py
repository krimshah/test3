from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import AdminMaster, CollegeMaster, DirectorMaster, GrievanceMaster, HODMaster, SolveGrievance, StudentMaster,TrustMaster,UniversityMaster,DepartmentMaster
from .forms import AdminMasterForm, CollegeMasterForm,UploadFileForm, DepartmentMasterForm, DirectorMasterForm, HODMasterForm, StudentMasterform, UniversityMasterEditForm,TrustMasterForm ,UniversityMasterForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import pandas as pd
import barcode
from barcode.writer import ImageWriter

# This is a All Message type .
# from django.contrib import messages
# from django.shortcuts import render, redirect

# def my_view(request):
#     # Some logic here...
#     messages.debug(request, 'This is a debug message.')
#     messages.info(request, 'This is an info message.')
#     messages.success(request, 'This is a success message.')
#     messages.warning(request, 'This is a warning message.')
#     messages.error(request, 'This is an error message.')
#     return redirect('some_url_name')

# Create your views here.
def home(request):
    return render(request,"forms.html",{'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def loginform(request):
    return render(request,'Login/login.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:  # Check if email and password are not empty
            try:
                admin = AdminMaster.objects.get(email_id=email)
                if password == admin.password :  # Check password using Django's check_password function
                    request.session['name'] = admin.name
                    request.session['id'] = admin.id
                    request.session['email'] = admin.email_id
                    request.session['role'] = 'Admin'  # Corrected typo
                    return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})  # Corrected duplicate key
                else:
                    return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
            except:
                try:
                    Trust = TrustMaster.objects.get(email = email)
                    if Trust.password == password:
                        request.session['name'] = Trust.name
                        request.session['id'] = Trust.trust_id
                        request.session['email'] = Trust.email
                        request.session['role'] = 'Trust'  
                        return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                    else:
                        return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
                except:
                    try:
                        University = UniversityMaster.objects.get(email = email,password=password)
                        if University:
                            request.session['name'] = University.university_name
                            request.session['id'] = University.university_id
                            request.session['email'] = University.email
                            request.session['role'] = 'University' 
                            return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                        else:
                            return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"})  
                    except:
                        try:
                            Collage = CollegeMaster.objects.get(email = email,password = password)
                            if Collage:
                                request.session['name'] = Collage.college_name
                                request.session['id'] = Collage.college_id
                                request.session['email'] = Collage.email
                                request.session['role'] = 'Collage' 
                                return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                            else:
                                return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
                        except:
                            try:
                                Dept=None
                                Dept = DepartmentMaster.objects.get(email=email,password=password)
                                if Dept != None:
                                    request.session['name'] = Dept.dept_name
                                    print('name',request.session.get('name'))
                                    request.session['id'] = Dept.department_id
                                    request.session['email'] = Dept.email
                                    request.session['role'] = 'Department' 
                                    return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                                else:
                                    return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
                            except:
                                try:
                                    Directer = None
                                    Directer = DirectorMaster.objects.get(email=email,password=password)
                                    if Directer != None:
                                        request.session['name'] = Directer.name
                                        request.session['id'] = Directer.director_id
                                        request.session['email'] = Directer.email
                                        request.session['role'] = 'Directer' 
                                        return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                                    else:
                                        return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
                                except:
                                    try:
                                        HOD = HODMaster.objects.get(email=email, password=password)
                                        if HOD:
                                            request.session['name'] = HOD.name
                                            request.session['id'] = HOD.hod_id
                                            request.session['email'] = HOD.email
                                            request.session['role'] = 'HOD'
                                            return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                                        else:
                                           return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
                                    except HODMaster.DoesNotExist:
                                        try:
                                            Student = StudentMaster.objects.get(email=email, password=password)
                                            if Student:
                                                request.session['name'] = Student.name
                                                request.session['id'] = Student.stu_id
                                                request.session['email'] = Student.email
                                                request.session['role'] = 'Student'
                                                request.session['Enrollment'] = Student.enrollment_no
                                                return render(request, 'forms.html', {'title': 'home', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
                                        except StudentMaster.DoesNotExist:
                                           return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"}) 
    else:
        return render(request,"Login/login.html",{'Error':"Enter a Valid Email and PAssword"})     

# This is a Logout Code.
def logout(request):
    # if del request.session['name'] and del request.session['id'] and del request.session['email'] and del request.session['role']:
    request.session.clear()
    return redirect("/")

    
    
    
    
# this is CRUD operations in Admin Panel.
def profile(request):
    # print(request.session.get('role'))
    try:
        if request.session.get('role') == "Admin":
            data = AdminMaster.objects.get(id=request.session.get('id'))
        elif request.session.get('role') == "Trust":
            data = TrustMaster.objects.get(trust_id=request.session.get('id'))
        elif request.session.get('role') == "University":
            data = UniversityMaster.objects.get(university_id=request.session.get('id'))
        elif request.session.get('role') == "Collage":
            data = CollegeMaster.objects.get(college_id=request.session.get('id'))
        elif request.session.get('role') == "Department":
            data = DepartmentMaster.objects.get(department_id=request.session.get('id'))
        elif request.session.get('role') == "Directer":
            data = DirectorMaster.objects.get(director_id=request.session.get('id'))
        elif request.session.get('role') == "HOD":
            data = HODMaster.objects.get(hod_id=request.session.get('id'))
        elif request.session.get('role') == "Student":
            data = StudentMaster.objects.get(stu_id=request.session.get('id'))
        # print(type(data.barcode))
        print(type(data))
        # print(data.college.college_name)
        # print(data.college.address_of_college)
        # check = SolveGrievance.objects.all()
        return render(request,"profile.html",{'title':"Profile",'data':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        return redirect('/home')

def formOfAddminAdd(request):
    form = AdminMasterForm()
    return render(request ,"admin/add.html",{'form' : form ,'title' : 'add Admin' , 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def storeAdmin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        email_id = request.POST.get('email_id') 
              
        AdminMaster.objects.create(name = name,password = password,email_id = email_id)
        return redirect("/home")
    else :
        return HttpResponse('The data could not be saved in the database.')        
def listAdminMaster(request):
    try: 
        # data = None
        data = AdminMaster.objects.all()
        if data != None :
            return render(request,'admin/showAdmin.html', {'data': data , 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
        return HttpResponse('The data could not be saved in the database.')
    except :
        return render(request,'admin/showAdmin.html', {'data': data , 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
            
def delAdminMAsterData(request,id):
    try:
        data = None
        data = AdminMaster.objects.filter(id = id).delete()
        if data != None :
            return redirect("/AdminMaster/show")
        return redirect('/AdminMaster/show')
    except:
        return get_object_or_404('Data Is not Delete')

def editAdminForm(request,id):
    if id != 0:
        try:    
            data_of_admin = AdminMaster.objects.get(id=id)
            
            return render(request,'admin/edit_admin.html', {'data':data_of_admin, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')}) 
        except:
            return redirect("/home")
    else:
        return HttpResponse("The Data Is Not Find")

def editAdmin(request):
    try:
        id = request.POST.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email_id = request.POST.get('email_id') 
        if id != 0:
            AdminMaster.objects.filter(id = id).update(name = name , email_id = email_id,password = password)
            return redirect("/AdminMaster/show")
        else:
            return redirect("/AdminMaster/show")
    except:
        return redirect("/home")
    
# This is a CRUD For the TrustMaster.
def TrustAddForm(request):
    data = TrustMasterForm()
    return render(request,"Trust/addtrust.html",{'data':data ,'title' : 'add Trust', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def StoreTrust(request):
    try:
        if request.method == "POST":
            Trust_name = request.POST.get('name')
            gov_reg_id = request.POST.get('gov_reg_id')
            password = request.POST.get('password')
            email = request.POST.get('email')
            form = TrustMasterForm(request.POST)
            if form.is_valid :
                form.save(commit=False)
                form.name = Trust_name
                form.gov_reg_id = gov_reg_id
                form.email = email
                form.password = password
                if form.save() :
                    return redirect('/TrustMaster/add')
            else:
                return HttpResponse("The Data Not Find")
        else:
            return HttpResponse("The Send Data Is Not Send Properly Go to Home Page <a href='/'> home</a>")
    except:
        return HttpResponse("The Method is not Call")

def ListTrustMaster(request):
    try:
        data = TrustMaster.objects.all()
        print("The Method is call")
        return render(request,'Trust/showTrust.html',{'data': data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')}) 
    except:
        return redirect("/home")
def DelTrust(request,id):
    if id != 0:
        data = TrustMaster.objects.filter(trust_id = id).delete()
        return redirect("/TrustMaster/show")
    else:
        return redirect("/home")
def TrustEditForm(request,id):
    if id != 0:
        try:
            data = TrustMaster.objects.get(trust_id = id)
            # print(data.name)
            return render(request,'Trust/EditTrust.html',{'data': data ,'title':'The Edit Form', 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
        except :
            return redirect("/home")

def EditTrust(request):
    try:
        id = request.POST.get("trust_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        gov_reg_id = request.POST.get("gov_reg_id")
        password = request.POST.get("password")
        if id != 0 and len(name) != 0 and len(email) != 0 and len(gov_reg_id) != 0 and len(password) != 0 :
           TrustMaster.objects.filter(trust_id = id).update(name = name,gov_reg_id = gov_reg_id,email = email,password = password)
           return redirect("/TrustMaster/show")
    except:
        return redirect("/home")

# This is a Crud For the University.
def AddFormUniversity(request):
    # data = UniversityMasterForm()
    trust = TrustMaster.objects.all()
    return render(request,"UniverSityMaster/addUniversityMaster.html",{'title' : 'Add University','trust':trust, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def addUniversity(request):
    if request.method == "POST":
        form = UniversityMasterForm(request.POST)
        if form.is_valid():
            # No need to extract form data manually, form.cleaned_data is used
            name = form.cleaned_data['university_name']
            email = form.cleaned_data['email']
            # logo = form.cleaned_data['logo']  # Use request.FILES to access uploaded files
            university_code = form.cleaned_data['university_code']
            password = form.cleaned_data['password']
            if(request.session.get('id') != 0):
                print(type(request.session.get('id')))
                trust_id = TrustMaster.objects.get(trust_id=request.session.get('id'))
            else:
                return redirect("/")
            # trustobj = trust_id
            
            if trust_id:
                # Create a UniversityMaster instance
                university_obj = UniversityMaster.objects.create(
                    university_name=name,
                    email=email,
                    # logo=logo,  # Assign the uploaded file directly
                    password=password,
                    trust=trust_id,
                    university_code=university_code
                )
                print("data is stored")
                return redirect("/UniversityMaster/AddForm")
    else:
        form = UniversityMasterForm()
    return redirect('/')

def showUniversity(request):
        data = UniversityMaster.objects.all()
        return render(request,'UniverSityMaster/showUniversity.html',{'data':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def delUniversity(request,id):
    try:
       UniversityMaster.objects.filter(university_id=id).delete() 
       messages.success(request,"The University Delete successfully")
       return redirect("/UniversityMaster/Show")
    except :
        messages.warning(request,"Unable To Delete University !")
        return redirect("/UniversityMaster/Show")
def editFromUniversity(request, id):
    data = UniversityMaster.objects.get(university_id=id)
    trust = TrustMaster.objects.all()
    return render(request, 'UniversityMaster/EditForm.html', {'title': 'The Data Is Stored', 'data': data, 'trust': trust, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def edituniversity(request):
    if request.method == "POST":
        # form = UniversityMasterEditForm(request.POST)
        if 1==1:
            # No need to extract form data manually, form.cleaned_data is used
            id = request.POST.get('university_id')
            print("The Id IS :",id)
            name = request.POST.get('university_name')
            email = request.POST.get('email')
            # logo = form.cleaned_data['logo']  # Use request.FILES to access uploaded files
            university_code = request.POST.get('university_code')
            password = request.POST.get('password')
            if(request.session.get('id') != 0):
                print(type(request.session.get('id')))
                trust_id = TrustMaster.objects.get(trust_id = request.session.get('id'))
            else:
                return redirect("/")
            print(f"id{id} name : {name} email :{email} university code : {university_code} password {password}")
            # print(id)
            # trustobj = trust_id
            if 1==1:
                # Create a UniversityMaster instance
                university_obj = get_object_or_404(UniversityMaster , university_id = id) 
                # university_obj.university_id = id 
                university_obj.university_name = name
                university_obj.email = email
                university_obj.password = password
                university_obj.university_code = university_code
                university_obj.trust = trust_id
                university_obj.save()
                messages.success(request,"The University Update successfully")
                return redirect("/UniversityMaster/Show")
            
            else:
                form = UniversityMasterForm()
                return redirect('/')

# This is code for the CRUD CollegeMaster.
def FormOfCollage(request):
    data = UniversityMaster.objects.all()
    if data:
        return render(request,'Collage/addClg.html',{'title':'Add Collage', 'university' : data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    return redirect("/home")

def addCollage(request):
     if request.method == "POST" :
        form = CollegeMasterForm(request.POST)
        if form.is_valid:
            college_name = request.POST.get('college_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address_of_college = request.POST.get('address_of_college')
            university_Id = request.session.get('id')
            print(university_Id)
            
            CollegeMaster.objects.create(
            college_name = college_name,
            email = email,
            password =password,
            address_of_college = address_of_college,
            university_Id_id = university_Id
            )
            return redirect("/CollageMaster/AddForm")
        return redirect("/home")

def delCollage(request,id):
    if id != 0:
        try:
            data = CollegeMaster.objects.get(college_id = id).delete()
            if data:
                return redirect("/CollageMaster/AddForm")
            else:
                pass
        except:
            return redirect("/home")
def showCollage(request):
    try:
        data = CollegeMaster.objects.filter(university_Id = request.session.get('id'))
        if data:
            return render(request,'Collage/showclg.html',{'title':"Collage Master",'data':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        return redirect("/home")


def editformClg(request,id):
    if id != 0:
        data = CollegeMaster.objects.get(college_id = id)
        university = UniversityMaster.objects.all()
        if data :
            return render(request,'Collage/edit.html',{'title':'Edit Collage Master','data': data,'university':university, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    else:
        return redirect("/home")

def editclg(request):
    if request.method == "POST" :
        form = CollegeMasterForm(request.POST)
        if form.is_valid:
            id = request.POST.get('id')
            college_name = request.POST.get('college_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address_of_college = request.POST.get('address_of_college')
            university_Id = request.session.get('id')
            # print(university_Id)
            data = UniversityMaster.objects.get(university_id = university_Id)
            print(type(data))
            collageupdate = get_object_or_404(CollegeMaster , college_id = id)           
            collageupdate.college_name = college_name
            collageupdate.email =email
            collageupdate.password = password
            collageupdate.address_of_college = address_of_college
            collageupdate.university_Id = data
            collageupdate.save()
            return redirect("/ColllageMaster/ShowCollage")
    else:
        return redirect("/home")
    

# This CRUD in DepartmentMaster.
def AddFormDept(request):
    # data = CollegeMaster.objects.all()
    return render(request,'Department/addDept.html',{'title':"Add Department", 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def addDept(request):
    if request.method == "POST" :
        dept_name = request.POST.get('dept_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        college = request.session.get('id')
        print(college)
        form = DepartmentMasterForm(request.POST)
        if form.is_valid:
            data = CollegeMaster.objects.get(college_id=college)
            DepartmentMaster.objects.create(
                dept_name = dept_name,
                email = email,
                password = password,
                college = data
            )            
            return redirect("/home")
        else:
            pass
    else:
        return redirect('/')

def showdept(request):
    try:
        print(request.session.get('id'))
        data = DepartmentMaster.objects.filter(college = request.session.get('id'))
        print('The Method is call')
        return render(request,'Department/showDept.html',{'title':'Department Master','dept':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        return redirect('/')
    
def deldept(request,id):
    if id != 0:
        DepartmentMaster.objects.filter(department_id = id).delete()
        return redirect('/DepartmentMaster/showDept')
    else:
        return redirect('/')

def editfromDept(request,id):
    if id != 0:
        data = DepartmentMaster.objects.get(department_id = id)
        clg = CollegeMaster.objects.all()
        return render(request,'Department/editdept.html',{'title': 'Edit Department Master','clg':clg,'data':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def editdept(request):
    if request.method == "POST" :
        form = DepartmentMasterForm(request.POST)
        if form.is_valid:
            department_id = request.POST.get('department_id')
            dept_name = request.POST.get('dept_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            college =  request.session.get('id')
            data = CollegeMaster.objects.get(college_id = college)
            print(type(data))
            collageupdate = get_object_or_404(DepartmentMaster, department_id = department_id)           
            collageupdate.dept_name = dept_name
            collageupdate.email =email
            collageupdate.password = password            
            collageupdate.college = data
            collageupdate.save()           
            return redirect("/DepartmentMaster/showDept")
    else:
        return redirect("/home")
    # This is a CRUD of Director Master
def adddirform(request):
    # data=DepartmentMaster.objects.all()
    return render(request,'Director/AddDirector.html',{"title":"Add Director Master", 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def storedirect(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.session.get('id')       
        form=DirectorMasterForm()
        if form.is_valid:
            data = DepartmentMaster.objects.get(department_id =department)
            DirectorMaster.objects.create(
                name=name,
                email =email,
                password =password,
                department = data
            )
            return redirect("/home")
        return redirect("/home")
    else:
        pass

def showdirecter(request):
    try:
        data = DirectorMaster.objects.filter(department=request.session.get('id'))
        if data :
            return render(request,'Director/showDir.html',{'title':"directer Master",'Directer':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        return redirect("/home")
    
def delDir(request,id):
    if id != 0 :
        DirectorMaster.objects.get(director_id=id).delete()
        return redirect("/Director/showdir")
    else:
        return redirect("/Director/showdir")
def editFormOfDir(request,id):
    data = DirectorMaster.objects.get(director_id=id)
    if data :
        return render(request,'Director/editfromDireccter.html',{'title':'Edit Directer Master','data':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def editDirecter(request):
    if request.method == "POST" :
        form = DirectorMasterForm(request.POST)
        if form.is_valid:
            director_id = request.POST.get('director_id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            department = request.session.get('id')
            data = DepartmentMaster.objects.get(department_id = department)
            print(type(data))
            collageupdate = get_object_or_404(DirectorMaster, director_id = director_id)           
            collageupdate.name = name
            collageupdate.email =email
            collageupdate.password = password            
            collageupdate.department = data
            collageupdate.save()           
            return redirect("/Director/showdir")
    else:
        return redirect("/home")
    
    # This is CRUD in HOD
def addFormHOD(request):
    # data = DirectorMaster.objects.all()
    return render(request,'HOD/addHOD.html',{'title':"Add Head Of Department", 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def storeHOD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        director =request.session.get('id')      
        form=HODMasterForm()
        if form.is_valid:
            data = DirectorMaster.objects.get(director_id =director)
            HODMaster.objects.create(
                name=name,
                email =email,
                password =password,
                director = data
            )
            return redirect("/home")
        return redirect("/home")
    else:
        pass
def showHod(request):
    try:
        data = HODMaster.objects.filter(director=request.session.get('id'))
        if data:
            return render(request,'HOD/showHOD.html',{'title':"Head Of Department Master(HOD)",'hod':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
        else:
           return render(request,'HOD/showHOD.html',{'title':"Head Of Department Master(HOD)",'hod':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        return redirect("/")

def delHOD(request,id):
    if id != 0:
        # print("kanji")
        print(id)
        data = HODMaster.objects.get(hod_id = id)
        print(data.name)
        data.delete()
        messages.success(request,"The Hod Is Deleted.")
        return redirect('/HODMaster/ShowHOD')
    else:
        return HttpResponse("The Id Is Not Valid Check Back.")
    
def editFormOfHOD(request,id):
    if id != 0:
        data = HODMaster.objects.get(hod_id = id)
        # dir = DirectorMaster.objects.all()
        if data :
            return render(request,'HOD/editForm.html',{'title':'Edit Head Of Department','data':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
        else:
            return redirect('/HODMaster/ShowHOD')
    else:
        return redirect('/')
    
def editHOD(request):
    if request.method == "POST" :
        form = HODMasterForm(request.POST)
        if form.is_valid:
            hod_id = request.POST.get('hod_id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            director = request.session.get('id')
            data = DirectorMaster.objects.get(director_id = director)
            print(type(data))
            collageupdate = get_object_or_404(HODMaster, hod_id = hod_id)           
            collageupdate.name = name
            collageupdate.email=email
            collageupdate.password = password            
            collageupdate.director = data
            collageupdate.save()           
            return redirect("/HODMaster/ShowHOD")
    else:
        return redirect("/home")
    
    # this is a CRUD Of StudentMaster
def addStudentForm(request):
    data = HODMaster.objects.all()
    if data:
        return render(request,'Student/addStuent.html',{'title':' Add New Student','hod': data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    
def storeStudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        enrollment_no = request.POST.get('enrollment_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hod_id = request.session.get('id')        
        form=StudentMasterform()
        if form.is_valid:
            data = HODMaster.objects.get(hod_id =hod_id)
            StudentMaster.objects.create(
                name=name,
                email = email,
                password =password,
                enrollment_no = enrollment_no,
                hod_id = data
            )
            return redirect("/home")
        return redirect("/home")
    else:
        pass

def showstudent(request):
    try:
        print(request.session.get('id'))
        data =  StudentMaster.objects.filter( hod_id = request.session.get('id'))
        return render(request,'Student/showstudent.html',{'title':'Student Master','student':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except :
        return redirect('/')
def showstu(request):
    try:
        data = StudentMaster.objects.all()
        return render(request,'Student/showstudent.html',{'title':'Student Master','student':data, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except :
        return redirect('/home')


def DelStudent(request,id):
    if id!=0:
        StudentMaster.objects.get(stu_id=id).delete()
        return redirect("/StudentMaster/showStudent")
    else:
        return redirect("/home")
def editFormStudent(request,id):
    if id != 0:
        data = StudentMaster.objects.get(stu_id=id)
        hod = HODMaster.objects.all()
        return render(request,'Student/editstudent.html',{'title':'Edit Student Master','data':data,'hod':hod, 'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    else:
        return redirect("/home")
    
def UpdateStudent(request):
    if request.method == "POST":
        form = StudentMasterform(request.POST)
        if form.is_valid:
            stu_id = request.POST.get('stu_id')
            name = request.POST.get('name')
            enrollment_no = request.POST.get('enrollment_no')
            email = request.POST.get('email')
            password = request.POST.get('password')
            hod_id = request.POST.get('hod_id')
            data = HODMaster.objects.get(hod_id = hod_id)
            print(type(data))
            Updatestu = get_object_or_404(StudentMaster, stu_id = stu_id)           
            Updatestu.name = name
            Updatestu.enrollment_no =enrollment_no
            Updatestu.email=email
            Updatestu.password = password            
            Updatestu.hod_id = data
            Updatestu.save()           
            return redirect("/StudentMaster/showStudent")
    else:
        return redirect("/home")
# This is crud of grievance MAster.
def grievanceForm(request):
    return render(request,"Grievance/addGrievance.html",{'title':"Grievance",'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def addgriv(request):
    if request.method == "POST":
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        id = request.session.get('id')
        data =  StudentMaster.objects.get(stu_id = id) 
        print(type(data))
        sender = data.stu_id
        hod_Fk = data.hod_id
        GrievanceMaster.objects.create(
            sender = data,
            Enrollment = data.enrollment_no,
           semester =semester,
            subject =subject,
            message=message,
            hod_Fk=hod_Fk,
            directer_Fk =data.hod_id.director,
            department_Fk =data.hod_id.director.department,
            collage_Fk =data.hod_id.director.department.college,
            university_Fk=data.hod_id.director.department.college.university_Id,
            trust_Fk=data.hod_id.director.department.college.university_Id.trust
        )
        return redirect("/home")
def showgrievance(request):
    try:
        if request.session.get('role') == "Admin":
            data = GrievanceMaster.objects.all()
        elif request.session.get('role') == "Trust":
            data = GrievanceMaster.objects.filter(trust_Fk=request.session.get('id'))
        elif request.session.get('role') == "University":
            data = GrievanceMaster.objects.filter(university_Fk=request.session.get('id'))
        elif request.session.get('role') == "Collage":
            data = GrievanceMaster.objects.filter(collage_Fk=request.session.get('id'))
        elif request.session.get('role') == "Department":
            data = GrievanceMaster.objects.filter(department_Fk=request.session.get('id'))
        elif request.session.get('role') == "Directer":
            data = GrievanceMaster.objects.filter(directer_Fk=request.session.get('id'))
        elif request.session.get('role') == "HOD":
            data = GrievanceMaster.objects.filter(hod_Fk=request.session.get('id'))
        elif request.session.get('role') == "Student":
            data = GrievanceMaster.objects.filter(sender=request.session.get('id'))
        check = SolveGrievance.objects.all()
        return render(request,"Grievance/ShowGrievance.html",{'title':"Grievance",'data':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role'),'check':check})
    except:
        return render(request,"Grievance/ShowGrievance.html",{'title':"Grievance",'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
def Check_grav(request,id):
    try:
        # check = SolveGrievance.objects.get(GrievanceId=id)
        data = GrievanceMaster.objects.get(grievanceId=id)
        try:
            check = SolveGrievance.objects.get(GrievanceId = data.grievanceId)
            return render(request,"Grievance/singleGrievance.html",{'i':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role'),'check':check})
        except: 
            return render(request,"Grievance/singleGrievance.html",{'i':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

    except:
        return redirect("/grievanceMaster/ShowGriv")
def del_grav(request,id):
    try:
        GrievanceMaster.objects.get(grievanceId=id).delete()
        messages.success(request, 'The Grievance is Delete Successful')
        return redirect("/grievanceMaster/ShowGriv")
    except:
        messages.error(request, 'The Grievance is Delete Successful')
        return redirect("/grievanceMaster/ShowGriv")
def transeferGrav(request,id):
    try:
        if request.session.get('role') == "Trust":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.trust_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error("The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")
        
        elif request.session.get('role') == "University":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.university_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error("The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")

        elif request.session.get('role') == "Collage":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.collage_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error("The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")
        elif request.session.get('role') == "Department":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.department_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error("The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")
        elif request.session.get('role') == "Directer":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.directer_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error("The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")
        elif request.session.get('role') == "HOD":
            try:
                data = GrievanceMaster.objects.get(grievanceId = id)
                data.hod_Fk = None
                data.save()
                messages.success(request,'The grievance Forward Successfully')
                return redirect("/grievanceMaster/ShowGriv")
            except:
                messages.error(request,"The grievance Not Send!!")
                return redirect("/grievanceMaster/ShowGriv")
        messages.warning(request,"The grievance Not Send!!")
        return redirect("/grievanceMaster/ShowGriv")
    except:
        messages.warning(request,"The grievance Not Send!!")
        return redirect("/grievanceMaster/ShowGriv")
# This is a Solve Graviyanse MAster CRUD
def formsolvgrav(request,id):
    try:
        data = GrievanceMaster.objects.get(grievanceId=id)
        return render(request,'SolvegrievanceMaster/add.html',{'title':'SolveGrievance','data':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        messages.warning("Unable to Solve Try Again !")
        return redirect("/grievanceMaster/ShowGriv")
def addsolveGrav(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        solution = request.POST.get("solution")
        GrievanceId = request.POST.get('GrievanceId')
        dataGrav = GrievanceMaster.objects.get(grievanceId=GrievanceId)
        solver_name = request.session.get('name')
        solver_role = request.session.get('role')
        solver_Email = request.session.get('email')
        studentId = request.POST.get('studentId')
        print(studentId)
        dataStu = StudentMaster.objects.get(stu_id = studentId)
        try:
            SolveGrievance.objects.create(
                subject = subject,
                solution = solution,
                GrievanceId = dataGrav,
                solver_name = solver_name,
                solver_role = solver_role,
                solver_Email =solver_Email,
                studentId = dataStu
            )
            messages.success(request,"The Grievance Solved")
            return redirect('/grievanceMaster/ShowGriv')
        except:
            messages.warning(request,"Error")
            return redirect('/grievanceMaster/ShowGriv')
def showsinglesolvgrav(request,id):
    print(id)
    try:
        data = SolveGrievance.objects.get(GrievanceId = id)
        return render(request,'SolvegrievanceMaster/showgravshow.html',{'data':data,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})
    except:
        messages.warning(request,'The Request is in Progress!!')
        return redirect('/grievanceMaster/ShowGriv')
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import UploadFileForm
from .models import HODMaster, StudentMaster
import pandas as pd

def upload_student(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                name = row['Name']
                enrollment_no = row['Enrollment number']
                email = row['Email']
                password = row['Password']
                hod_name = row['HOD']  # Assuming 'HOD' column contains HOD names
                try:
                    hod = HODMaster.objects.get(name=hod_name)
                except ObjectDoesNotExist:
                    # Handle the case where HOD doesn't exist
                    # You can either skip this student or handle it as per your requirement
                    continue
                
                StudentMaster.objects.create(
                name=name,
                email = email,
                password =password,
                enrollment_no = enrollment_no,
                hod_id = hod
                )


                # student = StudentMaster(
                #     name=name,
                #     enrollment_no=enrollment_no,
                #     email=email,
                #     password=password,
                #     hod_id=hod
                # )
                # try:
                #     data = StudentMaster.objects.get(name=name,enrollment_no=enrollment_no,email=email,hod_id=hod)
                #     if data :
                #         return redirect("/home")
                # except:
                #     continue
                # student.save()
                
            return redirect("/home")
    else:
        form = UploadFileForm()
    return render(request, 'Student/uploadstudent.html', {'form': form,'name': request.session.get('name'), 'email': request.session.get('email'), 'id': request.session.get('id'), 'role': request.session.get('role')})

def index(request):
    return render(request, 'main_admin/index.html')

def generate_barcode(request, data):
    # Generate the barcode
    barcode_class = barcode.get_barcode_class('code39')
    barcode_instance = barcode_class(data, writer=ImageWriter())
    barcode_image = barcode_instance.render()

    # Return the barcode image as an HTTP response
    response = HttpResponse(content_type="image/png")
    barcode_image.save(response, "PNG")
    return response

def generate_barcode(self):
        # Generate barcode using python-barcode library
        code128 = barcode.get_barcode_class('code128')
        barcode_image = code128(self.barcode_data, writer=ImageWriter())
        barcode_path = f"media/barcodes/{self.id}"  # Save barcode image with product ID as filename
        barcode_image.save(barcode_path)
        return barcode_path

