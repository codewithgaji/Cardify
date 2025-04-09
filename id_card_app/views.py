from django.shortcuts import render

# importing decorators and response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from id_card_app.models import NIN_IDCard, Business_Id, Drivers_license
from .serializers import NINSerializer, Business_Serializer, Driver_Serializer
from rest_framework import status

# Create your views here.


# THIS ONES USE DECORATORS

# @api_view(['GET']) # Decorators to get some data
# def getData(request):
#  NIN = NIN_IDCard.objects.all() # Query the data set                                                                                                                                                 
#         serialize_nin = NINSerializer(NIN, many=True) # set a var_name and set it equals to the serializer class created and then pass in the query and set 'many= True'                                                                                                                                     

#         return Response(serialize_nin.data)
    

# @api_view(['POST'])
# def addData(request):
#     serializer = NINSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# NIN API view
class NINInfo(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                NIN = NIN_IDCard.objects.get(pk=id) # Query the data set                                                                                                                                                 
                serialize_nin = NINSerializer(NIN) # set a var_name and set it equals to the serializer class created and then pass in the query and set 'many= True'                                                                                                                                     
                return Response(serialize_nin.data)
            except NIN_IDCard.DoesNotExist:
                return Response({'error': 'NIN record not found'}, status=404)
        
        else:
            nin = NIN_IDCard.objects.all()
            serializer = NINSerializer(nin)
            return Response(serializer.data)
    
    def post(self, request):
         serializer = NINSerializer(data=request.data)
         if serializer.is_valid():
            instance = serializer.save()
            return Response({"id": instance.id}, status=status.HTTP_201_CREATED) # This returns the ID
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Drivers_license API view
class DriversInfo(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                license = Drivers_license.objects.get(pk=id) # Query the data set                                                                                                                                                 
                serialize_license = Driver_Serializer(license) # set a var_name and set it equals to the serializer class created and then pass in the query and set 'many= True'                                                                                                                                     
                return Response(serialize_license.data)
            except Driver_Serializer.DoesNotExist:
                return Response({'error': 'Drivers license record not found'}, status=404)
        
        else:
            license = Drivers_license.objects.all()
            serializer = Driver_Serializer(license)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = Driver_Serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({"id": instance.id}, status=status.HTTP_201_CREATED) # This returns the ID
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Business_ID API view
class BusinessInfo(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                business = Business_Id.objects.get(pk=id) # Query the data set                                                                                                                                                 
                business_serializer = Business_Serializer(business) # set a var_name and set it equals to the serializer class created and then pass in the query and set 'many= True'                                                                                                                                     
                return Response(business_serializer.data)
            except Business_Serializer.DoesNotExist:
                return Response({'error': 'Business Id record not found'}, status=404)
        
        else:
            business  = Business_Id.objects.all()
            serializer = Driver_Serializer(business)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = Business_Serializer(data=request.data)
        if serializer.is_valid():
           instance = serializer.save()
           return Response({"id": instance.id}, status=status.HTTP_201_CREATED) # This returns the ID
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def TestData(request):
     return render(request, "index.html")

def Docsdata(request):
    return render(request, "docs.html")
