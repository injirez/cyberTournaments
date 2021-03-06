from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dota
from .serializers import DotaListSerializer, DotaTestListSerializer
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse


class DotaListView(APIView):

    @swagger_auto_schema(operation_summary="This is all data from Dota db")

    def get(self, request):
        tournaments = Dota.objects.select_related('siteName', 'gameMode', 'links').all()
        serializer = DotaListSerializer(tournaments, many=True)

        return Response(serializer.data)


class DotaListViewSiteName(APIView):

    @swagger_auto_schema(operation_summary="This is all tournaments from specific site",
                         operation_description="Enter site name")
    def get(self, request, siteName):
        tournaments = Dota.objects.filter(siteName=siteName)
        serializer = DotaListSerializer(tournaments, many=True)

        return Response(serializer.data)

class DotaListViewStatus(APIView):

    @swagger_auto_schema(operation_summary="This is all tournaments with specific status",
                         operation_description="Enter status")
    def get(self, request, status):
        tournaments = Dota.objects.filter(status=status)
        serializer = DotaListSerializer(tournaments, many=True)

        return Response(serializer.data)

class DotaListViewTest(APIView):

    @swagger_auto_schema(operation_summary="This is data for tests")

    def get(self, request):
        tournaments = Dota.objects.all()
        serializer = DotaTestListSerializer(tournaments, many=True)

        return Response(serializer.data)

# class AddParticipant(APIView):
#
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         serializer = CreateParticipantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=self.get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)




























# cursor = connections['default'].cursor()
#
#
# def index(request):
#     cursor.execute('SELECT * FROM "Dota_dota"')
#     data = cursor.fetchall()
#     jsonData = []
#     for obj in data:
#         jsonData.append({"id": obj[0], "title": obj[1], "status": obj[2], "startTime": obj[3], "gameMode": obj[4],
#                           "participant": obj[5], "reward": obj[6], "siteName": obj[7], "link": obj[8],
#                           "dateTime": obj[9], "img": obj[10]})
#
#     return JsonResponse(jsonData, safe=False, json_dumps_params={'ensure_ascii': False})
#
# def byDateDota(request):
#     cursor.execute('SELECT * FROM "Dota_dota" ORDER BY "dateTime"')
#     data = cursor.fetchall()
#     jsonData = []
#     for obj in data:
#         jsonData.append({"id": obj[0], "title": obj[1], "status": obj[2], "startTime": obj[3], "gameMode": obj[4],
#                          "participant": obj[5], "reward": obj[6], "siteName": obj[7], "link": obj[8],
#                          "dateTime": obj[9], "img": obj[10]})
#
#     return JsonResponse(jsonData, safe=False, json_dumps_params={'ensure_ascii': False})
#
#
# def byRewardDota(request):
#     cursor.execute('SELECT * FROM "Dota_dota" ORDER BY "reward"')
#     data = cursor.fetchall()
#     jsonData = []
#     for obj in data:
#         jsonData.append({"id": obj[0], "title": obj[1], "status": obj[2], "startTime": obj[3], "gameMode": obj[4],
#                          "participant": obj[5], "reward": obj[6], "siteName": obj[7], "link": obj[8],
#                          "dateTime": obj[9], "img": obj[10]})
#     print(jsonData)
#
#     return JsonResponse(jsonData, safe=False, json_dumps_params={'ensure_ascii': False})
#     # return HttpResponse("Dota tournaments ordered by reward")


