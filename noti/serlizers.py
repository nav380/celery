
from rest_framework import serializers
from noti.models import Notification


class notiserlizers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"