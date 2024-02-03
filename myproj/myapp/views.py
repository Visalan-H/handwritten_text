from django.shortcuts import render

def home(request):
    return render(request,'base.html')

def handwritten_to_text(request):
    if request.method == 'POST':
        
        return render(request,'output.html')
