from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import barcode 
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# Admin Master Model
class AdminMaster(models.Model):
    id = models.AutoField( primary_key=True,  editable=False)
    name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    email_id = models.EmailField(unique=True, null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    # barcodeimage = models.ImageField(upload_to="AdminImg/",null=True)
    class Meta:
        db_table ='AdminMaster'
    def __str__(self):
        return self.name
    
# Trust Master Model
class TrustMaster(models.Model):
    trust_id = models.AutoField( primary_key=True,  editable=False)
    name = models.CharField(max_length=255, null=False)
    gov_reg_id = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='TrustMaster'
    def __str__(self):
        return self.name

# University Master Model
class UniversityMaster(models.Model):
    university_id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    # logo = models.ImageField(upload_to='university_logos/', null=True, blank=True)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    university_code = models.CharField(max_length=255, unique=True, null=False)
    trust = models.ForeignKey(TrustMaster, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='UniversityMaster'
    def __str__(self):
        return self.university_name
    
# College Master Model
class CollegeMaster(models.Model):
    college_id = models.AutoField(primary_key=True, editable=False)
    college_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)  
    address_of_college = models.TextField(null=True, blank=True)
    university_Id = models.ForeignKey(UniversityMaster, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='CollegeMaster'
    def __str__(self):
        return self.college_name
    

# Department Master Model
class DepartmentMaster(models.Model):
    department_id = models.AutoField( primary_key=True, editable=False)
    dept_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    college = models.ForeignKey(CollegeMaster, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='DepartmentMaster'
    def __str__(self):
        return self.dept_name
   

# Director Master Model
class DirectorMaster(models.Model):
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    # img = models.ImageField(upload_to='director_images/', null=True, blank=True)
    department = models.ForeignKey(DepartmentMaster, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='DirectorMaster'
    def __str__(self):
        return self.name

# HOD Master Model
class HODMaster(models.Model):
    hod_id = models.AutoField(primary_key=True,  editable=False)
    name = models.CharField(max_length=255, null=False)
    # image = models.ImageField(upload_to='hod_images/', null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)  # Ensure to hash password before saving
    director = models.ForeignKey(DirectorMaster, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='HODMaster'
    def __str__(self):
        return self.name
    
    # This is a StudentMaster Table For the student.
class StudentMaster(models.Model):
    stu_id = models.AutoField(primary_key=True )
    name = models.CharField(max_length=50 ,null=False)
    enrollment_no = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=50 , null= False)
    hod_id = models.ForeignKey( HODMaster, on_delete=models.CASCADE , null=False , db_column= 'hod_id')
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    barcode = models.ImageField(upload_to="StudentImg/",null=True,blank=True)
    class Meta:
        db_table ='StudentMaster'
    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        env = EAN(f"{self.enrollment_no}",writer=ImageWriter())
        buffer = BytesIO()
        env.write(buffer)
        self.barcode.save('barcode.png',File(buffer),save=False)
        return super().save(*args, **kwargs)
# This is a GrievanceMaster.
class GrievanceMaster(models.Model):
    grievanceId = models.AutoField(primary_key=True ,editable=False )
    sender = models.ForeignKey(StudentMaster , on_delete=models.CASCADE , null= True)
    Enrollment = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], null= True)
    hod_Fk = models.ForeignKey(HODMaster ,  on_delete=models.CASCADE , null= True)
    directer_Fk = models.ForeignKey(DirectorMaster ,  on_delete=models.CASCADE , null= True)
    department_Fk = models.ForeignKey( DepartmentMaster, on_delete=models.CASCADE , null= True)
    semester = models.CharField(max_length=50 , null= False)
    subject = models.CharField(max_length=100 , null= True)
    message = models.CharField(max_length=200)
    collage_Fk = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null= True)
    university_Fk = models.ForeignKey(UniversityMaster, null= True, on_delete=models.CASCADE)
    trust_Fk = models.ForeignKey(TrustMaster, null= True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta :
        db_table = 'GrievanceMaster'
    def __str__(self):
        return self.Enrollment
    
class SolveGrievance(models.Model):
    solvGrievanceId = models.AutoField(primary_key=True,editable=False)
    subject = models.CharField(null=True, max_length=150)
    solution = models.CharField(max_length=200,null=True)
    GrievanceId = models.ForeignKey(GrievanceMaster,on_delete=models.CASCADE,null=False)
    # Statement = models.CharField(max_length=300 , null=False)
    solver_name = models.CharField(null=True,max_length=50,db_column='solver_name')
    solver_role = models.CharField(null=True,max_length=30,db_column='solver_role')
    solver_Email = models.CharField(null=True,max_length=50,db_column='solver_Email')
    studentId = models.ForeignKey(StudentMaster,on_delete=models.CASCADE,null=True,db_column='student')
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='SolveGrievance'
    def __str__(self) :
        return self.solver_Email

