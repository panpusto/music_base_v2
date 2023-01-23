from rest_framework import serializers
from albums.models import (
    Album,
    ALBUM_TYPES,
    FORMAT_TYPES,
)
from bands.models import (
    Band,
    BAND_STATUS
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


class BandSerializer(serializers.ModelSerializer):
    status = ChoiceField(choices=BAND_STATUS)
    genre = serializers.StringRelatedField(many=True)
    current_label = serializers.CharField(source='current_label.name')
    members = serializers.StringRelatedField(many=True)
    class Meta:
        model = Band
        fields = (
            'id',
            'name',
            'country_of_origin',
            'location',
            'status',
            'formed_in',
            'ended_in',
            'genre',
            'lyrical_themes',
            'current_label',
            'bio',
            'members'
        )