from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Details(models.Model):
	hospital = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	patient_name= models.CharField(max_length=200)
	patient_illness = models.TextField()
	admit_date = models.DateTimeField(default=timezone.now)
	discharge_date = models.DateTimeField(blank=True, null=True)
	attending_doctor_name= models.CharField(max_length=200)
	allocated_bed=models.IntegerField()
	def AllocateBed(self):
		self.free_beds-=1
class ResourceDetails(models.Model):
	total_beds=models.IntegerField(default=0)
	total_nonMed_staff=models.IntegerField(default=0)