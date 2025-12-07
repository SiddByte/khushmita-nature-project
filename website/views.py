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


from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings

def contect1(request):
    if request.method == "POST":

        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            first_name=first_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        # ✅ Send Email
        full_message = f"""
        Name: {first_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}

        Message:
        {message}
        """

        send_mail(
            subject=f"New Contact Form: {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('/contect/')

    return render(request, 'website/contact.html')


