from django.shortcuts import render

# Create your views here.
def main(request):
    fruit=["사과","배","감","귤"]
    context={"fruit":fruit}
    return render(request, "secondapp/index.html",context)

