import requests
from django.conf import settings
def imgbb(image_file):

    url = "https://api.imgbb.com/1/upload"
    api_key = settings.imgbb_key

    files = {
        "image": image_file.file  # 핵심: Django 업로드 파일에서 .file을 꺼냄
    }

    response = requests.post(url, files=files, data={"key": api_key})
    response_data = response.json()

    return response_data["data"]["url"]
