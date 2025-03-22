from django.shortcuts import render

# importing decorators and response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from id_card_app.models import NIN_IDCard, Business_Id, Drivers_license
from .serializers import NINSerializer, BusinessID, DriversLicense

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
    def get(self, request):
        NIN = NIN_IDCard.objects.all() # Query the data set                                                                                                                                                 
        serialize_nin = NINSerializer(NIN, many=True) # set a var_name and set it equals to the serializer class created and then pass in the query and set 'many= True'                                                                                                                                     

        return Response(serialize_nin.data)
    
    def post(self, request):
         serializer = NINSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()

         return Response(serializer.data)
    

# Drivers_license API view
class DriversInfo(APIView):
    def get(self, request):
        license = Drivers_license.objects.all()
        serializer = DriversLicense(license, many=True)

        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = DriversLicense(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Business_ID API view
class BusinessInfo(APIView):
    def get(self, request):
        business = Business_Id.objects.all()
        serializer = BusinessID(business, many=True)
        
        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = BusinessID(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

def TestData(request):
    return render(request, "index.html")
