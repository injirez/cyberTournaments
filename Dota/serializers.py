from rest_framework import serializers
from .models import Dota, Link, Reward


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('image', 'tournament')

class RewardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('type', 'count', 'currency')

class DotaListSerializer(serializers.ModelSerializer):
    siteName = serializers.SlugRelatedField(read_only=True, slug_field='name')
    gameMode = serializers.SlugRelatedField(read_only=True, slug_field='mode')
    links = LinkListSerializer(read_only=True)
    reward = RewardListSerializer(read_only=True)
    class Meta:
        model = Dota
        fields = ('title', 'status', 'startTime', 'gameMode', 'participant', 'reward', 'siteName', 'links', 'ip')

class DotaTestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dota
        fields = '__all__'

# #
# class CreateParticipantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dota
#         # fields = ("title", "img", "status", "startTime", "gameMode", "participant", "reward", "siteName", "link")
#         fields = ("title", "participant")

    # def create(self, validated_data):
    #     participantNum = Dota.objects.update_or_create(
    #         # id=validated_data.get('id', None),
    #         title=validated_data.get('title', None),
    #         # img=validated_data.get('img', None),
    #         # status=validated_data.get('status', None),
    #         # startTime=validated_data.get('startTime', None),
    #         # gameMode=validated_data.get('gameMode', None),
    #         # reward=validated_data.get('reward', None),
    #         # siteName=validated_data.get('siteName', None),
    #         # link=validated_data.get('link', None),
    #         # ip=validated_data.get('ip', None),
    #         defaults={'participant': validated_data.get("participant")}
    #     )

        # return participantNum
