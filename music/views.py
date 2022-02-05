# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render, redirect


# # imported our models
# from django.core.paginator import Paginator
# from . models import Song

# def Song(request):
#     # paginator= Paginator(Song.objects.all(),1)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#     # context={"page_obj":page_obj}
#     if request.method == "POST":
#         form = Song(request.POST,request.Files or None)
#         if form.is_valid():
#             form.save()
#             return HTTPResponse('Sucessfully Uploaded')
#     else:
#         form = Song()
#     return render(request,"music/song.html",{'form' : form})

# def specificsong(request, songname):
#     song = Song.objects.get(songName = songname)
#     context = {'song':song}
#     return render('music/song.html',context)

def song(request):
    return render('music/song.html')
