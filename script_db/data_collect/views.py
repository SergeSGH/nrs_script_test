from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Record
from .permissions import ReadOnly
from .serializers import RecordSerializer
from .tasks import check_deadlines, collect_data


class RecordViewSet(ReadOnlyModelViewSet):
    permission_classes = (ReadOnly,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @action(
        detail=False,
        methods=('get',),
        url_path='update_data',
        permission_classes=(ReadOnly,),
    )
    def update_data(self, request):
        collect_data.delay()
        return Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=('get',),
        url_path='update_deadlines',
        permission_classes=(ReadOnly,),
    )
    def update_deadlines(self, request):
        check_deadlines.delay()
        return Response(status=status.HTTP_200_OK)
