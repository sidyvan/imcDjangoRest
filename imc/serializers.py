from rest_framework import serializers

#CALCULA INDICE DE MASSA CORPORAL - IMC
class ImcSerializer(serializers.Serializer):

    peso = serializers.FloatField(min_value=0,)
    altura = serializers.FloatField(min_value=0,)
    resposta = serializers.SerializerMethodField()

    def get_resposta(self, obj):
    
        resposta = None
        peso = obj['peso']
        altura = obj['altura']
        imc = peso / (altura * altura)

        formatted_float_imc = "{:.2f}".format(imc)

        if(imc < 18.5):
            resposta = "MAGREZA : IMC = %s "%str(formatted_float_imc)
        elif(18.5 <= imc <= 24.9):
            resposta = "NORMAL: IMC = %s "%str(formatted_float_imc)
        elif(25.0 <= imc <= 29.9):
            resposta = "SOBREPESO:  IMC = %s "%str(formatted_float_imc)
        elif(30.0 <= imc <= 39.9):
            resposta = "OBESIDADE: IMC = %s "%str(formatted_float_imc)
        elif(40.0 < imc):
            resposta = "OBESIDADE GRAVE : IMC = %s "%str(formatted_float_imc)


        return resposta
