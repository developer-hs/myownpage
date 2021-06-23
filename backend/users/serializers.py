from django.db.models import fields
from rest_framework import serializers
from .models import User
from bookmark.models import BookmarkSites,  InputSite
from bookmark.serializers import BookmarkSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  "password", "first_name", "last_name", "residence"]
        read_only_fields = ("id",)
        # extra_kwargs = {'url': {'view_name': 'authentication:user-detail'}}

    def validate_first_name(self, value):
        return value.upper()

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        BookmarkSites.objects.create(user=user, locked="NAVER")
        user.bookmark.sites.add(InputSite.objects.get(name="NAVER"))
        return user
