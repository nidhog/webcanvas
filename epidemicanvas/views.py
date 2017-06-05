from django.http import HttpResponse, JsonResponse
from django.views import generic

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, api_view


from .models import Session, Artist, Contributions, Action
from .fields import ImageBase64Field
from .serializers import SessionSerializer, ArtistSerializer, ContributionSerializer, ActionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def partial_update(self, request, *args, **kwargs):
        print('***'*90)
        return super(SessionViewSet, self).partial_update(request, *args, **kwargs)

    @detail_route(methods=['post'])
    def set_name(self, request, pk=None):
        session = self.get_object()
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            session.name = serializer.data['name']
            session.save()
            return Response({'status': 'name set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def set_image(self, request, pk=None):
        session = self.get_object()
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            session.image = ImageBase64Field(
                        max_length=None, use_url=True, default=None
                 ).to_internal_value(request.data['image'])

            session.save()
            return Response({'status': 'image set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    @list_route()
    def recent_sessions(self, request):
        recent_sessions = Session.objects.all()

        page = self.paginate_queryset(recent_sessions)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_sessions, many=True)
        return Response(serializer.data)


class SessionUpdateName(generic.UpdateView):
    model = Session
    fields = ['id']
    template_name_suffix = '_update_form'


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.all()
    serializer_class = ContributionSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


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


def update_image(request):
    print('-'*200)
    print(request)
    print('-'*200)
    return HttpResponse("WOW.")


def index(request):
    return HttpResponse("Epidemic Paint Server.")


@api_view(['GET', 'POST'])
def get_actions(request):

    querydict = request.data
    last_date = querydict.get('last_created')
    session_id = querydict.get('session')
    if last_date and session_id:
        actions = Action.objects.filter(session=session_id, created__gt=last_date).order_by('created')
    elif session_id:
        actions = Action.objects.filter(session=session_id).order_by('created')
    else:
        actions = []

    action_list = [
        {
            'id' : action.id,
            'type': action.type,
            'session': action.session.id,
            'artist': action.artist.id,
            'startX': action.startX,
            'startY': action.startY,
            'endX': action.endX,
            'endY': action.endY,
            'created': action.created,
            'size': action.size,
            'color': action.color,
        }
        for action in actions
    ]
    return JsonResponse({'result': action_list})
