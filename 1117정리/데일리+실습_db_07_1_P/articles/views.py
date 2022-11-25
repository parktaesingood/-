from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                # 'created_at': article.created_at,
                # 'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles, fields=('title', 'content','created_at',))
    return HttpResponse(data, content_type='application/json')


@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
# 유효성 검사 통과 못했을 땐 serializer.errors임!
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE','PUT']) # PUT 써주고
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data) # drf 형태로 반환
    
    elif request.method == 'DELETE':
        article.delete()
        message = {
            'delete_message' : f'데이터 {article_pk}번 글이 삭제'
        }
        return Response(message,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': # ELIF 추가해주고
        serializer = ArticleSerializer(article, data=request.data) # POST와 다른점 새로운 데이터를 받아올 파라미터 하나 필요
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 댓글 리스트 조회
@api_view(['GET'])
def comments_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many =True)
    return Response(serializer.data)


# 댓글 조회 수정 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def comments_detail(request, comment_pk):
    pass



# 댓글 생성
@api_view(['POST'])
def comments_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','DELETE','PUT']) # PUT 써주고
def comments_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data) # drf 형태로 반환
    
    elif request.method == 'DELETE':
        comment.delete()
        message = {
            'delete_message' : f'데이터 {comment_pk}번 글이 삭제'
        }
        return Response(message,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': # ELIF 추가해주고
        serializer = CommentSerializer(comment, data=request.data) # POST와 다른점 새로운 데이터를 받아올 파라미터 하나 필요
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
