from django.shortcuts import render

# Create your views here.
def App1(request):
    data='Iam Fecting Data from Backend To Frond End By Using Jinger Tages(Context)'
    d={'App1':data}
    return render(request,'APP1.html',context=d)
def App2(request):
    d={'username':'Venkey'}
    return render(request,'App2.html',context=d) 