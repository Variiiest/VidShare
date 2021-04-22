from vlog.models import Video
from vlog.serializers import VideoSerializer
from rest_framework import mixins
from rest_framework import generics


class VlogList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Video.objects.all()
    serializer_class= VideoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class VlogDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset= Video.objects.all()
    serializer_class= VideoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
   
   
    
    

    