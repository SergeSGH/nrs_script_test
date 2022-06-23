from rest_framework import serializers

from .models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('id', 'num', 'order_num', 'cost', 'delivery_date', 'cost_rub')
