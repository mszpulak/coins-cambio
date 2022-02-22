from rest_framework.serializers import ModelSerializer, SlugRelatedField, IntegerField, PrimaryKeyRelatedField
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Coins


class CoinsSerializer(ModelSerializer):

    class Meta:
        model = Coins
        fields = '__all__'
        # read_only_fields = '__all__'


class AddCoinsSerializer(ModelSerializer):
    change_value = IntegerField(required=True, write_only=True)

    class Meta:
        model = Coins
        fields = ['change_value']

    def create(self, validated_data):
        return Coins.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.value = validated_data.get('change_value', 0) + instance.value if instance.value else instance.value
        instance.save()
        return instance


class UsersSerializer(ModelSerializer):
    users_coins = IntegerField(source='coins.value', read_only=True)
    username = serializers.CharField(read_only=True)
    change_value = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'users_coins', 'change_value']

    def update(self, instance, validated_data):
        print(validated_data)

        change = validated_data.pop('change_value', 0)
        if instance.coins:
            instance.coins.value += change
            instance.coins.save()
        else:
            Coins.objects.create(instance, value=change)
        return super().update(instance, validated_data)
