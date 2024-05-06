from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile('credentials.txt')


@csrf_exempt
def create_document(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            file_data = data.get('data')
            file_name = data.get('name')
            drive = GoogleDrive(gauth)
            file = drive.CreateFile({'title': file_name})
            file.SetContentString(file_data)
            file.Upload()
            return JsonResponse({'message': 'Загрузка успешна'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Метод не определен'}, status=400)
