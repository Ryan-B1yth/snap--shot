""" Imports """
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Static storage location """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Media storage location """
    location = settings.MEDIAFILES_LOCATION
