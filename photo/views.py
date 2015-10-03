from django.shortcuts import render
from django.http import HttpResponse

def single_photo(request, photo_id):
    return HttpResponse('{0}번 사진입니다'.format(photo_id))
