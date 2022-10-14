from django.forms import IntegerField
from rest_framework.serializers import (
    FileField, 
    Serializer,
    IntegerField,
)


class InputSerializer(Serializer):
    file = FileField()
    article = IntegerField()

    class Meta:
        fields = ["file", "article"]