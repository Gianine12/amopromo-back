from rest_framework import serializers

class AirportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    iata = serializers.CharField(max_length=3)
    city = serializers.CharField(max_length=3)
    lat = serializers.CharField(max_length=10) 
    lon = serializers.CharField(max_length=10) 
    state = serializers.CharField(max_length=2)
    obs = serializers.CharField(max_length=256) 
    active = serializers.BooleanField(default=True)
