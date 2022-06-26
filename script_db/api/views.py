from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from data_collect.models import Record
from data_collect.permissions import ReadOnly
from data_collect.serializers import RecordSerializer
from data_collect.tasks import check_deadlines, collect_data


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
        collect_data()
        return Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=('get',),
        url_path='update_deadlines',
        permission_classes=(ReadOnly,),
    )
    def update_deadlines(self, request):
        check_deadlines()
        return Response(status=status.HTTP_200_OK)
