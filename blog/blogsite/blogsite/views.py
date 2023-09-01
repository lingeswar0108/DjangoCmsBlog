from django.views import generic
from .models import posts,Contact
from django.shortcuts import render


   
class PostList(generic.ListView):
    queryset = posts.objects.filter(is_published=1).order_by('-created_date')
    template_name = 'index.html'
    

class PostDetail(generic.DetailView):
    model = posts
    template_name = 'post_detail.html'

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
    return render(request,'contact.html')


