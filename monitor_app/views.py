from rest_framework.response import Response
from rest_framework.decorators import api_view
import json # Libreria per manipolare dati JSON

# Create your views here.
@api_view(['POST'])
def receive_event(request):
    # API che riceve eventi in JSON, li interpreta e li stampa in console

    try:
        # Estrae i dati JSON dalla richiesta
        data = request.data

        # Stampa dell'evento ricevuto in formato leggibile nella console
        print('\nEvento ricevuto: ', json.dumps(data, indent=4))
        print('\n')

        # HTTP Response di conferma con i dati ricevuti
        return Response({"message": 'Evento ricevuto con successo', "data": data}, status=201)
    except Exception as e:
        # In caso di errore nel parsing dei dati, viene stampato l'errore e restituito un Error 400 (Bad Request)
        print("Error: ", str(e))
        return Response({"error:": 'Formato JSON non valido'}, status=400)
