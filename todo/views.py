from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects._create_user(request.POST['username'],email='noemail',password= request.POST['password1'],)
            user.save()
        else:
             pass ##tell the user password dont match