from unicodedata import name
from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    """Serialize a name field for testing API"""
    name = serializers.CharField(max_length=18)