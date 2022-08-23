# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customers


class CustomerViews(APIView):

    def get(self, request, id = None):
        if id:
            item = Customers.objects.get(customer_id = id)
            serializer = CustomerSerializer(item)
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        item = Customers.objects.all()
        serializer = CustomerSerializer(item, many = True)
        return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status= status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status= status.HTTP_400_BAD_REQUEST)