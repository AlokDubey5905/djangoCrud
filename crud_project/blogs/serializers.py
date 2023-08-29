# serializers.py
from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User  # Import the User model
from .models import Comment


# blog model serializer
class BlogSerializer(serializers.ModelSerializer):

    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'author_username', 'name', 'title',
                  'content', 'created_at']  # Include the new field

    def get_author_username(self, obj):
        # Retrieve the username from the User model associated with the author
        return obj.author.username if obj.author else None

# comments models serializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
