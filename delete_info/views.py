from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from generate_cv.models import Info

# Create your views here.
def delete(request, id):
    try:
        info = get_object_or_404(Info, id=id)
        info.delete()
        messages.success(request, 'CV deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting CV: {str(e)}')
    
    return redirect('home:index')