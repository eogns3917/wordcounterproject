from django.shortcuts import render
from .models import Login

# Create your views here.
def login(request):
    text='Login'
    context = {'text' : text}
    return render(request, "login.html", context)

def check(request):

    user_id = request.GET.get('id')
    user_pwd = request.GET.get('pwd')
    print(user_id)
    print(user_pwd)

    user_infos = Login.objects.all()

    for user_info in user_infos :
        if(user_info.identity == user_id and user_info.password == user_pwd) :
            text = "로그인 성공"
            break
        else : 
            text = "로그인 실패"
        
        context = {'text' : text}
    return render(request, "check.html", context)