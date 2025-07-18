from django.shortcuts import render, redirect
from generate_cv.models import Info
import json

# Create your views here.
def insert(request):
    return render(request, 'insert_info/index.html')

def insert_info(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        position = request.POST['position']
        # json encode full_name and position
        basics = {'full_name': full_name, 'position': position}
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        address = request.POST['address']
        contacts = {'email': email, 'phone': phone, 'website': website, 'address': address}
        languages = request.POST.get('languages')
        profile = request.POST.get('profile')
        skills = json.loads(request.POST.get('skills', '{}'))
        projects = json.loads(request.POST.get('projects', '{}'))
        education = json.loads(request.POST.get('education', '{}'))
        experience = json.loads(request.POST.get('experience', '{}'))

        photo = request.FILES['photo']

        # Process the form data and save it to the database
        try:
            data = Info.objects.create(
                basics=basics,
                contacts=contacts,
                skills=skills,
                projects=projects,
                education=education,
                experience=experience,
                photo=photo,
                languages=languages,
                profile=profile
            )
            return redirect('home:index')  # Redirect to home page after successful creation
        except Exception as e:
            return render(request, 'insert_info/index.html', {'error': str(e)})
            
    return render(request, 'insert_info/index.html')
