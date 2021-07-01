from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connections
import json


def index(request):
    cursor = connections['default'].cursor()
    cursor.execute('SELECT * FROM "Dota_dota"')
    data = cursor.fetchall()
    json_data = []
    for obj in data:
        json_data.append({"id": obj[0], "title": obj[1], "status": obj[2], "startTime": obj[3], "gameMode": obj[4],
                          "participant": obj[5], "reward": obj[6], "siteName": obj[7], "link": obj[8],
                          "dateTime": obj[9], "img": obj[10]})

    return JsonResponse(json_data, safe=False)
    # return HttpResponse(json.dumps(json_data, ensure_ascii=False))

def byDateDota(request):
    return HttpResponse('Dota tournaments ordered by date')


def byRewardDota(request):
    return HttpResponse("Dota tournaments ordered by reward")
