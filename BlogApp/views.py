from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination


class BlogView(APIView):
    def get(self, request):
        articles = Blog.objects.all()
        paginator = PageNumberPagination()
        posts = paginator.paginate_queryset(queryset=articles, request=request)
        data = {}
        data['posts'] = BlogSerializer(posts, many=True, context={'request': request}).data
        data['total'] = articles.count()
        data['next'] = paginator.get_next_link()
        data['previous'] = paginator.get_previous_link()
        return Response(data=data, status=status.HTTP_200_OK)


class SinglePost(APIView):
    def get(self, request, pk):
        article = Blog.objects.get(id=pk)
        data = BlogSerializer(article, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AllCategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        post = Blog.objects.filter(category=category)

        data = {}

        data['posts'] = BlogSerializer(post, many=True, context={'request': request}).data
        data['category'] = CategorySerializer(instance=category).data
        return Response(data=data, status=status.HTTP_200_OK)


class Recent(APIView):
    def get(self, request):
        recent = Blog.objects.all()[:3]
        data = BlogSerializer(recent, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class Popular(APIView):
    def get(self, request):
        popular = Blog.objects.filter(popular=True)[:3]
        data = BlogSerializer(popular, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
