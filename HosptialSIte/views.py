from django.shortcuts import render
from .forms import updateData
# Create your views here.
def patient_new(request):
    if request.method == "POST":
        form = updateData(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = updateData()
    return render(request, 'newPatient.html', {'form': form})