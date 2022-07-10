from re import I
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(max_length=255)
  number_of_pages = serializers.IntegerField()
  quantity = serializers.IntegerField(default=0)
  description = serializers.CharField(max_length=1000)
  created_at = serializers.DateTimeField(auto_now_add=True)
  updated_at = serializers.DateTimeField(auto_now=True)