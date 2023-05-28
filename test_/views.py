from django.shortcuts import render

# Create your views here.


def render_test_template(request):
    return render(request, "test_.html", {})