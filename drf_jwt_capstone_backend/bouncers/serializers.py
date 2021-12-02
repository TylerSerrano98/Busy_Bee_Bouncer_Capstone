from drf_jwt_capstone_backend.bouncers.models import Bouncer
from rest_framework import serializers
from .models import Bouncer


class BouncerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bouncer
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('name', 'price', 'dimensions', 'description')
