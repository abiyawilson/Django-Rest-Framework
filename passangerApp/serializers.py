from rest_framework import serializers

from passangerApp.models import Passanger


class PassagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = '__all__'
