from django.contrib import admin

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'order_num',
        'cost',
        'delivery_date',
        'cost_rub',
    )
    search_fields = (
        'num',
        'order_num',
        'cost',
        'delivery_date',
        'cost_rub',
    )
    list_filter = (
        'delivery_date',
    )
    list_editable = (
        'order_num',
        'cost',
        'delivery_date',
        'cost_rub',
    )
    empty_value_display = '--empty--'


admin.site.register(Record, RecordAdmin)
