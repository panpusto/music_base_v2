from rest_framework import serializers
from django.contrib.auth import get_user_model
from albums.models import (
    Album,
    ALBUM_TYPES,
    FORMAT_TYPES
)
from bands.models import (
    Band,
    BAND_STATUS
)
from labels.models import (
    Label,
    LABEL_STATUS
)
from musicians.models import (
    Musician
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


class LabelSerializer(serializers.ModelSerializer):
    status = ChoiceField(choices=LABEL_STATUS)
    class Meta:
        model = Label
        fields = (
            'id',
            'name',
            'address',
            'country',
            'status',
            'styles',
            'founding_year'
        )


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            'id',
            'name',
            'full_name',
            'born',
            'died',
            'place_of_birth',
            'bio'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
        )