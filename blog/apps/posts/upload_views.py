import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@csrf_exempt
@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        
        # Guardar archivo
        filename = default_storage.save(f'uploads/{upload.name}', ContentFile(upload.read()))
        file_url = settings.MEDIA_URL + filename
        
        # Respuesta para CKEditor
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': {'message': 'Error al subir archivo'}})