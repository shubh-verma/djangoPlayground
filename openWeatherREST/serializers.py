from rest_framework import serializers


class WeatherResponseSerializer(serializers.Serializer):
    cod = serializers.CharField()
    message = serializers.IntegerField()
    cnt = serializers.IntegerField()
    list = serializers.ListField()
    # WeatherDataSerializer(many=True)
    # city = CitySerializer()
