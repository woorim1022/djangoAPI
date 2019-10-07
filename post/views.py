#from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
#from django.http import Http404
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework import mixins
#from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers
from django.http import HttpResponse
# Create your views here.


#viewset
###
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #custom api
    def highlight(self, request, *args, **kwargs):
        post = self.get_object()
        return HttpResponse("얍")

#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)







#generic
###
#class PostList(generics.ListCreateAPIView): #불필요하게 중복되는 함수 선언들을 포함하고 있음
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#class PostDetail(generics.RetrieveUpdateDestroyAPIView): #불필요하게 중복되는 함수 선언들을 포함하고 있음
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer




#mixins
###
#class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs) 

#    def post(self, request, *args, **kwargs):
#       return self.create(request, *args, **kwargs)

#class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)

#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)





#APIview
###
#class PostList(APIView):
#    def get(self, request):
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(serializer.data)

#    def post(self, request):
#        serializer = PostSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class PostDetail(APIView):
#    def get_object(self, pk):
#        try:
#            return Post.objects.get(pk=pk)
#        except Post.DoesNotExist:
#            raise Http404

#    def get(self, request, pk, format=None):
#        post = self.get_object(pk)
#        serializer = PostSerializer(post)
#        return Response(serializer.data)

#    def put(self, request, pk, format=None):
#        post = self.get_object(pk)
#        serializer = PostSerializer(post, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
#        post = self.get_object(pk)
#        post.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)