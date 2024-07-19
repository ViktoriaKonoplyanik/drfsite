
from rest_framework import generics, status, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


#class WomenAPIView(generics.ListAPIView):
 #   queryset = Women.objects.all()
  #  serializer_class = WomenSerializer





    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #
    #
    #     if not pk:
    #         return Women.objects.all()[:3]
    #
    #     return Women.objects.filter(pk=pk)

    #
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name })





class WomenAPIList(generics.ListCreateAPIView):
     queryset = Women.objects.all()
     serializer_class = WomenSerializer
     permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
     queryset = Women.objects.all()
     serializer_class = WomenSerializer
     permission_classes = (IsAuthenticated, )
     #authentication_classes = (TokenAuthentication, )



class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
     queryset = Women.objects.all()
     serializer_class = WomenSerializer
     permission_classes = (IsAdminOrReadOnly, )


#class WomenAPIView(APIView):
#    def get(self, request):
#        w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTPP_400_BAD_REQUEST)
#         try:
#             instance = Women.objects.get(pk=pk).delete()
#             return Response({'message':f'Data from the id {str(pk)} has been deleated '}, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({"error": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
#







