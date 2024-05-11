from rest_framework import serializers
from .models import *


class FacebookGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookGroup
        fields = ['name', 'description', 'member_count', 'is_private', 'town', 'location']
        