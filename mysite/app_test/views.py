from django.shortcuts import render

def post_list(request):
    return render(request, 'app_test/post_list.html')