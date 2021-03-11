from rest_framework import serializers
from RESTJoinTables.models import JoinTablesmodel

class JoinTableSerialize(serializers.ModelSerializer):
    class Meta:
        model= JoinTablesmodel
        fields= '__all__'