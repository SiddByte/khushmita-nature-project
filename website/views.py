from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Contact
# blog/views.py
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render, get_object_or_404


class PostListView(ListView):
    model = Post
    template_name = 'website/blog.html'
    context_object_name = 'posts'
    paginate_by = 6  # posts per page

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-published_at')
    

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'website/blog_detail.html', {'post': post})




def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contect1(request):
    return render(request, 'website/contact.html')

def service(request):
    return render(request, 'website/service.html')

def causes(request):
    return render(request, 'website/causes.html')

def events(request):
    return render(request, 'website/events.html')



def contect1(request):
    if request.method == "POST":
        Contact.objects.create(
            first_name = request.POST.get('first_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        return redirect('/contect/')  # ya same page

    return render(request, 'website/contact.html')

