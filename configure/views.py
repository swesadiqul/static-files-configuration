from django.shortcuts import render

# Create your views here.
def home_view(request):
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('password')
        check = request.GET.get('check')
        print(email)
        print(password)
        print(check)
    return render(request, template_name="index.html")