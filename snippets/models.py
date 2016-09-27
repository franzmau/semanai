#coding:utf-8
import datetime

import django.db.models
import django.contrib.auth.models
from django.db import models
from snippets import common
# Create your models here.

class Usuario(django.db.models.Model):

    correo = django.db.models.CharField(
        max_length=255,
        verbose_name=common.MODEL_FIELD__CORREO
    )
    is_active = django.db.models.BooleanField(
        default=True,
        verbose_name=common.MODEL_FIELD__IS_ACTIVE
    )

    puntos = django.db.models.IntegerField(
        blank=True,
        verbose_name=common.MODEL_FIELD__Puntos
    )

    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=django.db.models.PROTECT,
        related_name=common.MODEL_RELATED__ACCOUNT,
        verbose_name=common.MODEL_NAME__USER
    )
    class Meta:
        verbose_name = common.MODEL_NAME__ACCOUNT
        verbose_name_plural = common.MODEL_NAME_PLURAL__ACCOUNT
    def __unicode__(self):
        return unicode(self.user.get_full_name())


class Genero(django.db.models.Model):

    titulo = django.db.models.CharField(
        max_length=500,
        verbose_name=common.MODEL_FIELD__Title
    )
    is_active = django.db.models.BooleanField(
        default=True,
        verbose_name=common.MODEL_FIELD__IS_ACTIVE
    )
    class Meta:
        verbose_name = common.MODEL_NAME__genero
        verbose_name_plural = common.MODEL_NAME_PLURAL__genero

class Libro(django.db.models.Model):
    titulo = django.db.models.CharField(
        max_length=500,
        verbose_name=common.MODEL_FIELD__Title
    )
    autor = django.db.models.CharField(
        max_length=500,
        verbose_name=common.MODEL_FIELD__Author,
        blank=True
    )
    descripcion = django.db.models.CharField(
        verbose_name=common.MODEL_FIELD__Descripcion,
        max_length=255
    )
    is_active = django.db.models.BooleanField(
        default=True,
        verbose_name=common.MODEL_FIELD__IS_ACTIVE
    )
    foto = django.db.models.CharField(
        verbose_name=common.MODEL_FIELD__Photo,
        max_length=255
    )

    genero = django.db.models.ForeignKey(
        Genero,
        on_delete=django.db.models.PROTECT,
        related_name=common.MODEL_RELATED__Libro,
        verbose_name=common.MODEL_NAME__genero
    )


    class Meta:
        verbose_name = common.MODEL_lIBRO_
        verbose_name_plural = common.MODEL_NAME_PLURAL__Libro


class Pregunta(django.db.models.Model):
    pregu = django.db.models.CharField(
        max_length=500,
        verbose_name=common.MODEL_FIELD__Pregunta
    )

    rc = django.db.models.CharField(
        max_length=500,
        blank=True
    )

    r= django.db.models.CharField(
        max_length=255,
    )

    is_active = django.db.models.BooleanField(
        default=True,
        verbose_name=common.MODEL_FIELD__IS_ACTIVE
    )

    r2 = django.db.models.CharField(
        max_length=255,

    )
    r3 = django.db.models.CharField(
        max_length=255,
    )

    libro = django.db.models.ForeignKey(
        Libro,
        on_delete=django.db.models.PROTECT,
        related_name=common.MODEL_RELATED__Libro,
        verbose_name=common.MODEL_NAME__Pregunta
    )
    class Meta:
        verbose_name = common.MODEL_Pregunta_
        verbose_name_plural = common.MODEL_NAME_PLURAL__Pregunta


class Cupon(django.db.models.Model):
    nombre = django.db.models.CharField(
        max_length=500,
        verbose_name=common.MODEL_FIELD__NOmbre
    )

    puntos = django.db.models.IntegerField(
        blank=True,
        verbose_name=common.MODEL_FIELD__Puntos
    )

    Descripcion= django.db.models.CharField(
        max_length=255,
        verbose_name=common.MODEL_FIELD__Descripcion
    )

    is_active = django.db.models.BooleanField(
        default=True,
        verbose_name=common.MODEL_FIELD__IS_ACTIVE
    )


    class Meta:
        verbose_name = common.MODEL_Cupon_
        verbose_name_plural = common.MODEL_NAME_PLURAL__Cupones




