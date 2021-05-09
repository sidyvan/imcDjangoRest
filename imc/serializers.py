from rest_framework import serializers


class ImcSerializer(serializers.Serializer):

    peso = serializers.FloatField()
    altura = serializers.FloatField()
    imc = serializers.SerializerMethodField()

    def get_imc(self, obj):
        peso = obj['peso']
        altura = obj['altura']
        imc = peso / (altura * altura)

        return imc
