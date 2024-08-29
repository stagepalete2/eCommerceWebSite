from django.shortcuts import render

from .forms import SignInForm

# Create your views here.
def profile(request):
    return render(request, template_name='profile.html')

def edit_profile(request):
    return render(request, template_name='edit.html')

def signin(request):
    form = SignInForm
    context = {
        'form' : form,
    }
    return render(request, template_name='auth/signin.html', context=context)


def signup(request):
    return render(request, template_name='auth/signup.html')