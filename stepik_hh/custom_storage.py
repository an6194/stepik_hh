from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'media'  # store user files under directory `media/` in bucket


class StaticStorage(S3Boto3Storage):
    location = 'static'  # store static files under directory `static/` in bucket
