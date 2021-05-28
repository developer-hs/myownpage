import notepad
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .views import NotePads


class NotePadSerializer(ModelSerializer):

    class Meta:
        model = NotePads
        fields = ("id","memo", "datetime_created", "datetime_update")
        read_only_fields = ("id" ,)
        
    def create(self, validated_data):
        user = self.context.get("user")
        memo = (validated_data.get("memo"))
        NotePads.objects.create(memo = memo ,user=user)
        return NotePads
