from rest_framework import serializers
from .models import Otter


class OtterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'image_url', 'created_at')
        model = Otter

