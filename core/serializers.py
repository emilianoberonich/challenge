from rest_framework import serializers
from . import models


class PhysicianSerializer(serializers.ModelSerializer):
    '''Serializes physician objects'''

    class Meta:
        model = models.Physician
        fields = ('id', 'name_given', 'name_family', 'title', 'clinic')
