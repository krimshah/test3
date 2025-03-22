from django import forms
from .models import AdminMaster, StudentMaster, TrustMaster , UniversityMaster , CollegeMaster , DepartmentMaster , DirectorMaster , HODMaster,GrievanceMaster
# this is for the AdminMaster
class AdminMasterForm(forms.ModelForm):
    class Meta:
        model = AdminMaster
        fields = ['name','password','email_id']


# this is for the TrustMaster
class TrustMasterForm(forms.ModelForm):
    class Meta:
        model = TrustMaster
        fields = ['name','gov_reg_id','email','password']
# this is for the UniversityMaster
class UniversityMasterForm(forms.ModelForm):
    class Meta:
        model = UniversityMaster
        fields = ['university_name','email','password','university_code']
# This is a use to edit the University
class UniversityMasterEditForm(forms.ModelForm):
    class Meta:
        model = UniversityMaster
        fields = ['university_id','university_name','email','password','university_code']


# this is for the CollegeMaster
class CollegeMasterForm(forms.ModelForm):
    class Meta:
        model = CollegeMaster
        fields = ['college_name','email','password','address_of_college']

# this is for the DepartmentMaster
class DepartmentMasterForm(forms.ModelForm):
    class Meta:
        model = DepartmentMaster
        fields = ['dept_name','email','password']

# this is for the DirectorMaster
class DirectorMasterForm(forms.ModelForm):
    class Meta:
        model = DirectorMaster
        fields = ['name','email','password']

# this is for the HODMaster
class HODMasterForm(forms.ModelForm):
    class Meta:
        model = HODMaster
        fields = ['name','email','password']

# This is for the Student MAster
class StudentMasterform(forms.ModelForm):
    class Meta:
        model = StudentMaster
        fields = ['name','enrollment_no','email','password','hod_id']

# This is for the Student MAster
class GrievanceMasterform(forms.ModelForm):
    class Meta:
        model = GrievanceMaster
        fields = ['semester','subject','message']

class UploadFileForm(forms.Form):
    file = forms.FileField()