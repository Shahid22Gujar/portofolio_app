from django.shortcuts import render

# Create your views here.
def serve(request):
    context = {'services':'active'}
    return render(request,'services/services.html',context)