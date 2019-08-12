from rest_framework import serializers
from .models import logEntry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = logEntry
        fields = ('ua','ip','val')
