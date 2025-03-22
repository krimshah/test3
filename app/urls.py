"""
URL configuration for gms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.urls import path

urlpatterns = [
   path('home',views.home,name="home"),
   path("profile",views.profile, name="profile"),
#    This is a CRUD on The AdminMaster.
    # path("AdminMaster/Profile",views.profileAdmin, name="adminProfile")
    # path("prfile/", .as_view(), name="")
    path('AdminMaster/add',views.formOfAddminAdd,name='addadmin'),
    path('storeAdmin',views.storeAdmin,name='storeAdmin'),
    path("AdminMaster/show", views.listAdminMaster, name="LastAdminMaster"),
    path("DelAdmin/<int:id>",views.delAdminMAsterData,name='delAdmin'),
    path("AdminMaster/EditForm/<int:id>",views.editAdminForm,name="EditAdminForm"),
    path("AdminMaster/Edit",views.editAdmin,name="EditAdmin"),
#    this is for practise perpuse.
    path('index',views.index,name="index"),
# This is a CRUD on The TrustMaster.
    path('TrustMaster/add',views.TrustAddForm,name="addTrust"),
    path("TrustStore",views.StoreTrust,name="add"),
    path("TrustMaster/show",views.ListTrustMaster,name="showtrust"),
    path("DelTrust/<int:id>",views.DelTrust,name="deleteTrust"),
    path("TrustMaster/EditForm/<int:id>",views.TrustEditForm,name="editTrustFrom"),
    path("EditTrust",views.EditTrust,name="editTrust"),
    # This is a CRUD on the UniversityMster.
    path("UniversityMaster/AddForm",views.AddFormUniversity,name="addFromuniversity"),
    path("UniversityMaster/Add",views.addUniversity,name="adduniversity"),
    path("UniversityMaster/Show",views.showUniversity,name="showUniversity"),
    path("DelUniversity/<int:id>", views.delUniversity, name="delUniversity"),
    path("UniversityMaster/EditForm/<int:id>", views.editFromUniversity, name="EditFormUniversity"),
    path("EditUniversity",views.edituniversity,name="edituniversity"),
    # This is a CRUD on the CollageMaster.
    path('CollageMaster/AddForm',views.FormOfCollage,name="addclg"),
    path('CollageMaster/CollageStore',views.addCollage,name="addcolage"),
    path("ColllageMaster/ShowCollage",views.showCollage,name="showclg"),
    path("delCollageMaster/<int:id>",views.delCollage,name="delclg"),
    path("ColllageMaster/CollageEditForm/<int:id>",views.editformClg, name="editclgform"),
    path("ColllageMaster/EditClg", views.editclg, name="editclg"),
    # This is CRUD of DepartmentMaster 
    path('DepartmentMaster/addFormOfDept',views.AddFormDept,name='AddFormDept'),
    path('DepartmentMaster/storeDept',views.addDept,name='addDept'),
    path('DepartmentMaster/showDept',views.showdept,name='showdept'),
    path('DepartmentMaster/delDept/<int:id>',views.deldept,name='deldept'),
    path('DepartmentMaster/DeptEditForm/<int:id>',views.editfromDept,name='editFormDept'),
    path('DepartmentMaster/Editdept',views.editdept,name='editdept'),
    # This is a CRUD Of Directer
    path('Director/AddDirector',views.adddirform,name='Adddept'),
    path("Director/adddir", views.storedirect, name="storeddirecter"),
    path('Director/showdir',views.showdirecter,name="showdirecter"),
    path('Director/delDir/<int:id>',views.delDir,name="deldirecter"),
    path("Director/EditDirecter/<int:id>",views.editFormOfDir,name='editFormOfDir'),
    path('Director/EditDir',views.editDirecter,name='editDirecter'),
    # This is a CRUD in HODMaster
    path('HODMaster/AddForm',views.addFormHOD,name='addHODForm'),
    path('HODMaster/StoreHOD',views.storeHOD,name='addhod'),
    path('HODMaster/ShowHOD',views.showHod,name='showHOD'),
    path("HODMaster/delHod/<int:id>", views.delHOD,name='delhod'),
    path('HODMaster/EditHod/<int:id>',views.editFormOfHOD,name='editform'),
    path('HODMaster/EditHod',views.editHOD,name='editHOD'),
    # This is a CRUD for the 
    path("StudentMaster/addStudent",views.addStudentForm,name="addstudent"),
    path('StudentMaster/storeStudent',views.storeStudent,name='storestudent'),
    path("StudentMaster/showStudent",views.showstudent, name="showstudent"),
    path("showstuwithuniversity", views.showstu, name="showstuuniv"),
    path("StudentMaster/DelStudent/<int:id>", views.DelStudent, name="delStudent"),
    path("StudentMaster/EditStudentForm/<int:id>", views.editFormStudent, name="editFormStu"),
    path("StudentMaster/EditStudent/", views.UpdateStudent, name="editStudent"),
    # this is aLogin Logic 
    path("Login", views.login, name="login"),
    path("",views.loginform,name='loginForm'),
    # This is a Logout Page
    path("Logout",views.logout, name="logout"),
    # this is a crud for the grievance Master.
    path("grievanceMaster/AddForm", views.grievanceForm, name="grievanceForm"),
    path("AddGriev",views.addgriv,name="addgriv"),
    path("grievanceMaster/ShowGriv",views.showgrievance,name="showgriv"),
    path("grievanceMaster/Detailgrievance/<int:id>", views.Check_grav, name="demo"),
    path("grievanceMaster/delgrievance/<int:id>", views.del_grav, name="delgriv"),
    path("grievanceMaster/TranferGrav/<int:id>", views.transeferGrav, name="transferGrav"),
    # This is a SelveGAraviyanse crud .
    path("SolvegrievanceMaster/addSolve/<int:id>", views.formsolvgrav, name="addsolv"),
    path("SolvegrievanceMaster/Store", views.addsolveGrav, name="addsolvgrav"),
    path("SolvegrievanceMaster/show/<int:id>", views.showsinglesolvgrav, name="showsolvgrav"),
    # This is url for the add student with excel
    path("excelStudent", views.upload_student, name="excel"),
    
    path('generate-qr-code', views.generate_barcode, name='generate_qr_code'),

]