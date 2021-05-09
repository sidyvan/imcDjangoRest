from rest_framework import serializers


class ImcSerializer(serializers.Serializer):

    peso = serializers.FloatField()
    altura = serializers.FloatField()
    imc = serializers.SerializerMethodField()

    def get_imc(self, obj):
        resposta = None

        peso = obj['peso']
        altura = obj['altura']
        imc = peso / (altura * altura)

        if(imc < 18.5):
            resposta = "MAGREZA"
        elif(18.5 <= imc <= 24.9):
            resposta = "NORMAL"
        elif(25.0 <= imc <= 29.9):
            resposta = "SOBREPESO"

        elif(30.0 <= imc <= 39.9):
            resposta = "OBESIDADE"

        elif(40.0 < imc):
            resposta = "OBESIDADE GRAVE"




        return resposta
