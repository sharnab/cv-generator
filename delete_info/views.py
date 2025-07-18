from django.shortcuts import render

# Create your views here.
def delete(request):
    return render(request, 'delete_info/index.html')