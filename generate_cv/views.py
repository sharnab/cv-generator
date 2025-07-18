from django.shortcuts import render, get_object_or_404
from .models import Info
import json

def generate(request, id=None):
    if id:
        data = get_object_or_404(Info, id=id)
        
        # Convert the data to JSON strings
        skills_json = json.dumps(data.skills) if data.skills else '{"ops":[]}'
        projects_json = json.dumps(data.projects) if data.projects else '{"ops":[]}'
        education_json = json.dumps(data.education) if data.education else '{"ops":[]}'
        experience_json = json.dumps(data.experience) if data.experience else '{"ops":[]}'
        
        context = {
            'data': data,
            'basics': data.basics,
            'contacts': data.contacts,
            'languages': data.languages,
            'skills_json': skills_json,
            'projects_json': projects_json,
            'education_json': education_json,
            'experience_json': experience_json,
        }
        return render(request, 'generate_cv/index.html', context)
    return render(request, 'home/index.html', {'error': 'Invalid ID'})