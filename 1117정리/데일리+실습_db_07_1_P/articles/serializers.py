from rest_framework import serializers
from .models import Article ,Comment

class ArticleListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Article
        fields = ('title','content',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # article은 유효성검사하지 않아도 된다
        
        
class ArticleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source= ' comments.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'