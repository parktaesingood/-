## 10/21 프로젝트

* 역참조
review는 movie를 참조한다. 만약 리뷰가 무비를 역참조 하려고 하면 review라는 related_name을 쓴다.
```python
 movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='review')
```


```python
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='review')
```
> 왜 serializer.save(movie=movie)인거지
```python
@api_view(['POST'])
def reviews_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

시리어라이즈 할 때 가져오는 movie_pk 파라미터를 movie에 저장해주어야 연걸됨
```python
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='review')
```
Review 클래시는 title, content, movie 있어야하니까.

