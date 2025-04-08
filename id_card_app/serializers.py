from rest_framework import serializers
from id_card_app.models import NIN_IDCard, Drivers_license, Business_Id


# We are creating a serializer so we can turn instances of our models into readable data                                                                                                                                                                                                                                                                                   

class NINSerializer(serializers.ModelSerializer):
    class Meta: # inner meta class
        model = NIN_IDCard # This is for the model name 
        fields = '__all__' # this serializes all the fields

class Driver_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers_license
        fields = '__all__'


class Business_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Id
        fields = '__all__'
