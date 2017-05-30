from django.core.files.base import ContentFile
from rest_framework import serializers

import base64


class ImageBase64Field(serializers.ImageField):
    def from_native(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            image_format, image_string = data.split(';base64,')
            extension = image_format.split('/')[-1]

            data = ContentFile(base64.b64decode(image_string), name='temp.' + extension)

        return super(ImageBase64Field, self).from_native(data)
