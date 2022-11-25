from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    
    if request.method == 'GET':
        book = get_list_or_404(Book)
        serializer = BookListSerializer(book,many=True)
        return Response(serializer.data)
    
    # Q 2.
    elif request.method == 'POST':
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    book = get_object_or_404(Book,pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    # Q 4.
    
    elif request.method == 'DELETE':
        book.delete()
        serializer = BookSerializer(book)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    # Q 5.
    elif request.method == 'PUT':
        serializer = BookSerializer(book,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def comment_list(request):
    # Q 7.
    comment = get_list_or_404(Comment)
    if request.method == 'GET':
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    comment = Comment.objects.all(request,book_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment=comment)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    # Q 10.
    
    elif request.method == 'DELETE':
        comment.delete()
        serializer = CommentSerializer(comment)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    

