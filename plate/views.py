import string
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Plate
from .serializers import PlateSerializer

letters = string.ascii_uppercase
numbers = string.digits

def generate_plate(format='LNNNLL'):
    plate = ''
    for i in format.upper():
        if i == 'L':
            plate+=random.choice(letters)
        elif i=='N':
            plate+=str(random.choice(numbers))
        else:
            plate+=i
    return plate
    



class GeneratePlateView(APIView):
    def get(self,request):
        numbers = set()
        params = request.query_params
        amount = params.get('amount',1)
        plate_format = params.get('plate_format','LNNNLL')
        amount = int(amount)
        for i in range(amount):
            number = generate_plate(plate_format)
            while number in numbers:
                number = generate_plate(plate_format)
            numbers.add(number)
        return Response(data=numbers)
        
class GetPlateView(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        plate = Plate.objects.get(id=id)
        serializer = PlateSerializer(plate)
        return Response(data=serializer.data)
class AddPlateView(APIView):
    def post(self,request):
        data = request.data
        format = data.get('format','LNNNLL').upper()
        plate = data['plate']
        if len(plate)!=len(format):
            return Response(data='This number is not valid.',status=status.HTTP_400_BAD_REQUEST)
        for i in range(len(format)):
            if format[i]=='L':
                if not plate[i].isalpha():
                    return Response(data='This number is not valid.',status=status.HTTP_400_BAD_REQUEST)
            elif format[i]=='N':
                if not plate[i].isdigit():
                    return Response(data='This number is not valid.',status=status.HTTP_400_BAD_REQUEST)
            elif format[i]!=plate[i]:
                return Response(data='This number is not valid.',status=status.HTTP_400_BAD_REQUEST)
        new_plate , created= Plate.objects.get_or_create(number=plate.upper())
        if not created:
            return Response(data='This number is already exist.',status=status.HTTP_400_BAD_REQUEST)
        serializer = PlateSerializer(instance=new_plate)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
