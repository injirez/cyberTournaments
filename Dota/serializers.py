from rest_framework import serializers
from .models import Dota

class DotaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dota
        fields = '__all__'

