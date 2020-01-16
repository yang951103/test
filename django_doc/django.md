# django

* Serializer字段为类变量，当字段为日期时，日期默认值只会被初始化一次。不是每次调用都会被初始化一次

* model_id_gen为函数，采用函数每次创建实例都会被调用，如果使用model_id_gen(),一次运行环境中，都是一样的。
class DjangoModel:
    id = models.CharField(verbose_name=u"设备 ID", primary_key=True, max_length=256, default=model_id_gen, help_text=u"主键")
