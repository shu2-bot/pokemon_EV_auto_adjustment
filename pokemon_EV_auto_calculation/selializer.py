"""
from rest_framework import serializers
from .models import DatabaseOne, DatabaseTwoChild
from .models import Move_Status
from rest_framework.validators import UniqueValidator # これは外部キーを使用している場合に使用します

class DatabaseTwoChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move_Status
        fields = "__all__"
    db2 = serializers.PrimaryKeyRelatedField(
        queryset = Move_Status.objects.using("move_status").all(),
        validators = [UniqueValidator(queryset = DatabaseTwoChild.objects.using("move_status").all())]
    )

   def create(self, data):
        save_data = DatabaseTwoChild(**data)
        save_data.save(using="database2")
        return save_data
"""
