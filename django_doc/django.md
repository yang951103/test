# django

* Serializer字段为类变量，当字段为日期时，日期默认值只会被初始化一次。不是每次调用都会被初始化一次

* model_id_gen为函数，采用函数每次创建实例都会被调用，如果使用model_id_gen(),一次运行环境中，都是一样的。
class DjangoModel:
    id = models.CharField(verbose_name=u"设备 ID", primary_key=True, max_length=256, default=model_id_gen, help_text=u"主键")

* editable为相对前端用户来讲不能写入和编辑，后端可以修改

* put和patch区别：put为幂等，patch可以幂等或不幂等。django中put需要添加所有必填字段，覆盖原有数据，没有的字段保留原本的值，patch不需要

* Department.objects.filter(parent_id__in=[1, None]), None会被忽略掉
Department.objects.filter(parent_id=None)可以找到parent_id为None情况，列表里会被忽略

* 请求可以传null，{"parent_id": null, "code": "k"} 对应字段null=True

* Model的Meta被转换为_meta,Serializer的Meta没有

* 环境变量的设置会覆盖代码中的settings文件路径设置