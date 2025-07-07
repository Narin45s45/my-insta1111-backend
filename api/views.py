import requests
from django.http import JsonResponse

def video_list(request):
                                            # آدرس API پربازدیدترین ویدیوهای آپارات
                                            aparat_api_url = "https://www.aparat.com/etc/api/mostviewedvideos"

                                            try:
                                                response = requests.get(aparat_api_url, timeout=10)
                                                response.raise_for_status() # کنترل خطاهای HTTP
                                                data = response.json()
                                                video_list_data = data.get('mostviewedvideos', [])
                                                return JsonResponse(video_list_data, safe=False)
                                            except requests.exceptions.RequestException as e:
                                                return JsonResponse({"error": str(e)}, status=500)