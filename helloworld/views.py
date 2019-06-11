from django.shortcuts import render

# Create your views here.
def home(request):
    text='main입니다.'
    context = {'text':text}
    return render(request, "HelloWorld.html",context)

def result(request):
    text=request.GET.get('text')
    wordcnt={}
    word=[]
    if text is not None:
        word=text.split(' ')
        for i in word:
            if i in wordcnt:
                wordcnt[i]=wordcnt[i]+1
            else:
                wordcnt[i]=1

   
    context = {'text':text,'word':word, 'wordcnt_item' : wordcnt.items()}
    return render(request, "HelloWorld.html",context)

def menu(request):
    text='menu입니다.'
    context = {'text':text}
    return render(request, "menu.html",context)