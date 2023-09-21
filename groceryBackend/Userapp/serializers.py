import django.db
from rest_framework import serializers
from Userapp.models import UserModel
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"