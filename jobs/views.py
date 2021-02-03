from django.shortcuts import render

from jobs.models import Jobs

# Create your views here.

def home_view(request):
    job = Jobs.objects.all()
    context = {'allJobs':job}
    return render(request,'jobs/home.html', context)

