from django.http import HttpResponse

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Session, Artist, Contributions
from .serializers import SessionSerializer, ArtistSerializer, ContributionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.all()
    serializer_class = ContributionSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    lookup_field = 'first_name'
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            artist = Artist.objects.create(**serializer.validated_data)
            return Response({**serializer.validated_data, **{'id': artist.id}}, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Artist could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("Epidemic Paint Server.")
