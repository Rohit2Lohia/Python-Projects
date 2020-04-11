from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            # log the user in
            login(request,user)
            # sending them a mail
            message='Now you can create your own blog entries! congratulations.'
            to=request.POST['email']
            send_mail('Welcome Onboard',message, settings.EMAIL_HOST_USER, [to],fail_silently=True)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login karo
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:list')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')
