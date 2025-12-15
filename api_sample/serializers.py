from rest_framework import serializers

from api_sample.models import StudentModel

class studentserializer(serializers.ModelSerializer):

    class Meta:

        model = StudentModel

        fields = "__all__"