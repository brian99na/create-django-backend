from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'user_name', 'bio')
        extra_kwargs = { 
            'password' : { 'write_only': True, 'min_length': 4 }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)