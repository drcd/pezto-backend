from rest_framework import serializers
from pastes.models import Paste


class PasteSerializer(serializers.Serializer):
    class Meta:
        model = Paste
        fields = ('title', 'content', 'date', 'url')
