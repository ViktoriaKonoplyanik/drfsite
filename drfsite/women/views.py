
from rest_framework import generics
from .models import Women
from .permissions import IsAdminOrReadOnly,
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated





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









