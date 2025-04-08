from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notification
from .serlizers import notiserlizers
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def notification_list(request):
    notifications = Notification.objects.filter(user_id=3)
    serializer = notiserlizers(notifications, many=True)
    
    
    return Response(serializer.data)
