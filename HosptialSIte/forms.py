from django import forms

from .models import Details,ResourceDetails

class updateData(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('patient_name','patient_illness','attending_doctor_name','allocated_bed',)