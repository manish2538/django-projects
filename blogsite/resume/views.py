from django.shortcuts import render
from datetime import datetime
from resume.models import Contact
from resume.models import Resume
from resume.models import Project
from resume.models import Post

from django.contrib import messages
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    resume= Resume.objects.get(pk=1)
    return render(request,"about.html",{"resume":resume})
def portfolio(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request,"portfolio.html",context)
    


#def blog(request):
#   context = {
 #       'posts' : Post.objects.all()
  #  }
   # return render (request,"blog.html",context)
    
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name,email=email ,phone = phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your form has been')

    return render(request,"contact.html")
    
class PostListView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = 'posts'

    ordering = ['-date']
