from django.shortcuts import render


def jinja(request):
    d={'name':'sanny','age':15}
    return render(request,'jinja.html',context=d)



# Create your views here.
