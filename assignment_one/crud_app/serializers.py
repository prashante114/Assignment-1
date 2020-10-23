from rest_framework import serializers 
from crud_app.models import RouterProperties





class RouterPropertiesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RouterProperties
        fields = ('sapid',
                  'hostname',
                  'loopback',
                  'macaddress')