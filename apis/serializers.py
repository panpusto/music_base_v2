from rest_framework import serializers
from albums.models import (
    Album,
    ALBUM_TYPES,
    FORMAT_TYPES,
)


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class AlbumSerializer(serializers.ModelSerializer):
    band = serializers.CharField(source='band.name')
    genre = serializers.StringRelatedField(many=True)
    album_type = ChoiceField(choices=ALBUM_TYPES)
    label = serializers.CharField(source='label.name')
    album_format = ChoiceField(choices=FORMAT_TYPES)
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'band',
            'genre',
            'album_type',
            'release_date',
            'catalog_id',
            'label',
            'album_format',
            'cover'
        )
