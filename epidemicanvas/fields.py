import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers


class ImageBase64Field(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            imgfmt, imgstr = data.split(';base64,')
            ext = imgfmt.split('/')[-1]
            uuid_id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name = uuid_id.urn[9:] + '.' + ext)
        return super(ImageBase64Field, self).to_internal_value(data)
