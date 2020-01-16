# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.auth.validators import ASCIIUsernameValidator


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(db_column='create_time', default=timezone.now)
    updated = models.DateTimeField(db_column='update_time', auto_now=True)


class Menu(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'menu'
        ordering = ['id']

    codename = models.CharField(verbose_name=u"菜单 code", max_length=128, unique=True, help_text=u"菜单 code")
    name = models.CharField(verbose_name=u"菜单名称", max_length=128, help_text=u"菜单名称")

    def __unicode__(self):
        return u"菜单:{}".format(self.name)


class MenuItem(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'menu_item'
        ordering = ['id']

    codename = models.CharField(verbose_name=u"功能 code", max_length=128, unique=True, help_text=u"功能 code")
    name = models.CharField(verbose_name=u"功能名称", max_length=128, help_text=u"功能名称")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent_item = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return u"功能:{}".format(self.name)


class Organization(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'organization'
        ordering = ['id']

    codename = models.CharField(verbose_name=u"组织 code", max_length=128, unique=True, help_text=u"组织 code")
    name = models.CharField(verbose_name=u"组织名称", max_length=255, help_text=u"组织名称")

    def __unicode__(self):
        return u"组织:{}".format(self.name)


class PlantOrganization(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'plant_organization'
        ordering = ['id']

    name = models.CharField(verbose_name=u"生产厂名称", max_length=255, help_text=u"生产厂名称")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    short_name = models.CharField(verbose_name=u"简称", max_length=255, help_text=u"简称")

    def __unicode__(self):
        return u"生产厂:{}".format(self.name)


class OrganizationAdmin(BaseModel):
    class Meta(BaseModel.Meta):
        db_table = 'organization_admin'
        ordering = ['id']

    username = models.CharField(
        max_length=12,
        validators=[ASCIIUsernameValidator(), MinLengthValidator(4)],
        unique=True)
    password = models.CharField(max_length=18, validators=[MinLengthValidator(4)])
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"组织账号:{}".format(self.username)
