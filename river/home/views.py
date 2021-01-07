import os

from django.http import FileResponse
from django.shortcuts import HttpResponse, render, redirect
from django.templatetags.static import static
from django.urls import reverse
import pafy
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from django.template.defaultfilters import filesizeformat
from PyPDF4 import PdfFileReader
from gtts import gTTS
from tempfile import TemporaryFile

# Create your views here.
def home(request):
    return render(request, 'home/Homepage.html')

# youtube video download.
def ytdownload(request):
    return render(request, 'youtubevideos/youtubedownload.html')

def download(request):
    global link
    link = request.GET.get('inputbox')
    if 'm.' in link:
            link = link.replace(u'm.', u'')

    elif 'youtu.be' in link:
            video_id = link.split('/')[-1]
            link = 'https://www.youtube.com/watch?v=' + video_id

    if len(link.split("=")[-1]) != 11:
            return HttpResponse('Enter correct url.')

    video = pafy.new(link)
    stream = video.streams
    video_audio_streams = []
    for s in stream:
        video_audio_streams.append({
            'resolution': s.resolution,
            'extension': s.extension,
            'file_size': filesizeformat(s.get_filesize()),
            'link': s.url + "&title=" + video.title
        })

    stream_video = video.videostreams
    video_streams = []
    for s in stream_video:
        video_streams.append({
            'resolution': s.resolution,
            'extension': s.extension,
            'file_size': filesizeformat(s.get_filesize()),
            'link': s.url + "&title=" + video.title
        })

    stream_audio = video.audiostreams
    audio_streams = []
    for s in stream_audio:
        audio_streams.append({
            'resolution': s.resolution,
            'extension': s.extension,
            'file_size': filesizeformat(s.get_filesize()),
            'link': s.url + "&title=" + video.title
        })

    context = {
        'title': video.title, 'streams': video_audio_streams,
        # 'description': video.description, 
        'likes': video.likes,
        'dislikes': video.dislikes, 'thumb': video.bigthumbhd,
        'duration': video.duration, 'views': video.viewcount,
        'stream_video': video_streams, 'stream_audio': audio_streams
        }

    return render(request, 'youtubevideos/youtubedownload.html', context)

# youtube tags show.
def youtubetags(request):
    return render(request, 'youtubetags/yttags.html')

def tagsget(request): 
    link1 = request.GET.get('inputbox1')
   
    if 'm.' in link1:
            link1 = link1.replace(u'm.', u'')

    elif 'youtu.be' in link1:
            video_id = link1.split('/')[-1]
            link1 = 'https://www.youtube.com/watch?v=' + video_id

    if len(link1.split("=")[-1]) != 11:
            return HttpResponse('Enter correct url.')

    request1 = requests.get(link1)
    html = BeautifulSoup(request1.content, "html.parser")
    tags = html.find_all("meta", property="og:video:tag")
    empty_tags = []
    for tag in tags:
        empty_tags.append(tag['content'])
    print(empty_tags)
    context = {'empty_tags': empty_tags}
    return render(request, 'youtubetags/youtubetagsget.html', context)

