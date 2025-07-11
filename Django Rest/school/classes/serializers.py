# Implement ClassroomSerializer Here
from rest_framework import serializers

from .models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"

    def validate_capacity(self, value):
        if value < 5:
            raise serializers.ValidationError("Error")
        return value

    def validate_area(self, value):
        if value < 0:
            raise serializers.ValidationError("Error")
        return value
