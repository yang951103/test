import datetime
from django.db import models
from rest_framework.utils.model_meta import get_field_info


def create_model_data(model, count=1, start_id=1, param_dict={}):
    # 自动创建测试数据
    fields = get_field_info(model).fields
    forward_relations = get_field_info(model).forward_relations
    cols = [{} for _ in range(count)]

    def add_value(key, val=None, func=int):
        for i in range(count):
            if key in param_dict:   # noqa
                cols[i][key] = param_dict.get(key)
            else:
                if val is None:
                    cols[i][key] = func(i + start_id)
                else:
                    cols[i][key] = val

    for k, v in fields.items():
        if c := v.choices:  # noqa
            add_value(k, c[0][0])
            continue
        if isinstance(v, models.CharField):
            add_value(k, None, str)

        elif isinstance(v, models.DateTimeField):
            if v.auto_now or v.auto_now_add:
                continue
            add_value(k, datetime.datetime.now())

        elif isinstance(v, models.DateField):
            if v.auto_now or v.auto_now_add:
                continue
            add_value(k, datetime.date.today())

        elif isinstance(v, (models.BooleanField, models.NullBooleanField)):
            add_value(k, False)

        elif isinstance(v, models.DurationField):
            add_value(k, datetime.timedelta())

        elif isinstance(v, models.ForeignKey):
            add_value(k + '_id')

        # note: Add other model.Field if needed
        else:
            add_value(k)

    for fk in forward_relations.keys():
        add_value(fk + '_id')

    for col in cols:
        print(col)
        model.objects.create(**col)
