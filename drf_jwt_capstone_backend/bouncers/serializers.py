
from rest_framework import serializers
from .models import Bouncer


class BouncerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bouncer
        fields = ('User','Items', 'Price', 'Dimensions', 'Description')
