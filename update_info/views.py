from django.shortcuts import render, get_object_or_404, redirect
from generate_cv.models import Info
from django.contrib import messages
import json

# Create your views here.
def update(request, id=None):
    #get data
    if id:
        data = get_object_or_404(Info, id=id)
        # Convert the data to JSON strings
        skills_json = json.dumps(data.skills) if data.skills else '{"ops":[]}'
        projects_json = json.dumps(data.projects) if data.projects else '{"ops":[]}'
        education_json = json.dumps(data.education) if data.education else '{"ops":[]}'
        experience_json = json.dumps(data.experience) if data.experience else '{"ops":[]}'
        
        context = {
            'id': id,
            'data': data,
            'basics': data.basics,
            'contacts': data.contacts,
            'languages': data.languages,
            'skills_json': skills_json,
            'projects_json': projects_json,
            'education_json': education_json,
            'experience_json': experience_json,
        }
        return render(request, 'update_info/index.html', context)
    return render(request, 'home/index.html', {'error': 'Invalid ID'})

def update_info(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            if not id:
                raise ValueError('ID is required')
                
            # Get the instance first
            info = Info.objects.get(id=id)
            
            # Update fields
            info.basics = {
                'full_name': request.POST['full_name'],
                'position': request.POST['position']
            }
            info.contacts = {
                'email': request.POST['email'],
                'phone': request.POST['phone'],
                'website': request.POST['website'],
                'address': request.POST['address']
            }
            info.languages = request.POST.get('languages')
            info.profile = request.POST.get('profile')
            info.skills = json.loads(request.POST.get('skills', '{}'))
            info.projects = json.loads(request.POST.get('projects', '{}'))
            info.education = json.loads(request.POST.get('education', '{}'))
            info.experience = json.loads(request.POST.get('experience', '{}'))

            # Handle photo upload
            if 'photo' in request.FILES:
                info.photo = request.FILES['photo']

            # Save the instance
            info.save()
            
            # Add success message
            messages.success(request, 'Info updated successfully!')
            return redirect('home:index')
            
        except Exception as e:
            return render(request, 'update_info/index.html', {'error': str(e)})
    
    return redirect('home:index')
