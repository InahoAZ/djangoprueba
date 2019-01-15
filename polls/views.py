from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def coso(request):
    query = Question.objects.all()
    return render(request, 'blog/coso.html', {'query': query})


def post_detail(request, pk):
    query = get_object_or_404(Question, pk=pk)
    return render(request, 'blog/post_detail.html', {'query': query})
