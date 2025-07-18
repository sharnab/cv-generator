from django.shortcuts import render
from generate_cv.models import Info
# Create your views here.
def index(request):
    #get data
    data = Info.objects.all()
    return render(request, 'home/index.html', {'data': data})