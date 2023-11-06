from rest_framework.decorators import api_view
from rest_framework.response import Response
from .modelo1 import predict

@api_view(['POST'])
def predict_view(request):
    data = request.data  # Asume que los datos se envían como JSON en el cuerpo de la solicitud
    prediction = predict(data)
    return Response(prediction.tolist())  # Convierte la predicción a JSON