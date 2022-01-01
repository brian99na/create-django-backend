from ..models.post import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = { 
            'file' : {'required': False, 'allow_null': True}
        }