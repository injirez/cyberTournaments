from rest_framework import serializers
from .models import Dota


class DotaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dota
        fields = '__all__'


class CreateParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dota
        # fields = ("title", "img", "status", "startTime", "gameMode", "participant", "reward", "siteName", "link")
        fields = ("title", "participant")

    def create(self, validated_data):
        participantNum = Dota.objects.update_or_create(
            # id=validated_data.get('id', None),
            title=validated_data.get('title', None),
            # img=validated_data.get('img', None),
            # status=validated_data.get('status', None),
            # startTime=validated_data.get('startTime', None),
            # gameMode=validated_data.get('gameMode', None),
            # reward=validated_data.get('reward', None),
            # siteName=validated_data.get('siteName', None),
            # link=validated_data.get('link', None),
            # ip=validated_data.get('ip', None),
            defaults={'participant': validated_data.get("participant")}
        )

        return participantNum
