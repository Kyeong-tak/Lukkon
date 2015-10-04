from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

def single_photo(request, photo_id):
    return HttpResponse('{0}번 사진입니다'.format(photo_id))

def post_list(request):
    posts = Photo.objects.all().order_by('published_date')
    return render(request, 'photo/index.html', {'posts' : posts})

