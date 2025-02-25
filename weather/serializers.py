from rest_framework import serializers


class ForecastResponseSerializer(serializers.Serializer):
    cod = serializers.CharField()
    message = serializers.IntegerField()
    cnt = serializers.IntegerField()
    list = serializers.ListField()


class WeatherSerializer(serializers.Serializer):
    coord = serializers.DictField()
    weather = serializers.ListField()
    # base = serializers.CharField()
    main = serializers.DictField()
    # visibility = serializers.IntegerField()
    # wind = WindSerializer()
    # rain = RainSerializer(required=False)
    # clouds = CloudsSerializer()
    # dt = serializers.IntegerField()
    # sys = SysSerializer()
    # timezone = serializers.IntegerField()
    id = serializers.IntegerField()
    # name = serializers.CharField()
    cod = serializers.IntegerField()
