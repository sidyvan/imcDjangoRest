from rest_framework import serializers


class ImcSerializer(serializers.Serializer):

    peso = serializers.FloatField()
    altura = serializers.FloatField()
    

