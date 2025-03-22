from django.contrib import admin
from .models import AdminMaster, CollegeMaster, DepartmentMaster, DirectorMaster, GrievanceMaster, HODMaster, StudentMaster, TrustMaster, UniversityMaster

# Register your models here.
admin.site.register(AdminMaster)
admin.site.register(TrustMaster)
admin.site.register(UniversityMaster)
admin.site.register(CollegeMaster)
admin.site.register(DepartmentMaster)
admin.site.register(DirectorMaster)
admin.site.register(HODMaster)
admin.site.register(StudentMaster)
admin.site.register(GrievanceMaster)
