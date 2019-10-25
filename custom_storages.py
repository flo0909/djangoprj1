from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# class for AWS media storage

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION