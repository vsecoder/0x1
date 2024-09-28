from tortoise import fields
from tortoise.models import Model


class File(Model):
    id = fields.BigIntField(pk=True, unique=True)
    sha256 = fields.CharField(max_length=255, null=True, unique=True)
    password = fields.CharField(max_length=255, null=True)
    # file mimetype
    mime = fields.CharField(max_length=255, null=True)
    # ip address
    addr = fields.CharField(max_length=255)
    # user agents
    ua = fields.CharField(max_length=255, null=True)
    removed = fields.BooleanField(default=False)
    expiration = fields.DatetimeField(null=True)
    # file size in bytes
    size = fields.BigIntField(null=True)

    # downloads count
    downloads = fields.IntField(default=0)
    # restores after expiration
    restores = fields.IntField(default=0)


class Blacklist(Model):
    id = fields.BigIntField(pk=True, unique=True)
    addr = fields.CharField(max_length=255, null=True)
