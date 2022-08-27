from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

from .utils import textOnImg

def front(request):
    return render(request, "index.html")


@api_view(["POST"])
# @csrf_exempt
def upload_Image(request):

    image = request.FILES.get('image')
    if image == None:
         return Response(status=400)
    sticker = textOnImg(text="hello Pushhy", image=image)
    response = Response(sticker.getvalue(), content_type='image/webp')
    response['Content-Disposition'] = 'attachment; filename="output.webp"'
    return response
