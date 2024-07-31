from django.shortcuts import render, redirect

from.models import Profile, Resume, Feedback,Project,Education,Skill
from .forms import FeedbackForm

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("home")# Redirect to a success page or another view
    else:
        form = FeedbackForm()

    profile_info = Profile.objects.get(pk=1)
    resume_file = Resume.objects.get(pk=3)
    education_info = Education.objects.all()
    skill_info = Skill.objects.all()
    project_info = Project.objects.all()
    context={'profile': profile_info,
             'resume':resume_file,
             'education':education_info,
             'skill': skill_info,
             'project': project_info,
             'contact_form':form
             }
    return render(request, "website/home.html",context)

