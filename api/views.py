from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer, SupplierSerializer
from .models import Item, Supplier

@api_view(['GET','POST'])
def items(request):
    if request.method=='GET':
        item=Item.objects.all()
        print(item)
        serializer=ItemSerializer(item, many=True)
        print(serializer)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','POST'])
def suppliers(request):
    if request.method=='GET':
        supplier=Supplier.objects.all()
        print(supplier)
        serializer=SupplierSerializer(supplier, many=True)
        print(serializer)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','DELETE','PUT'])
def item(request, pk):
    if request.method=='GET':
        item_instance=Item.objects.get(id=pk)
        serializer=ItemSerializer(item_instance)
        return Response(serializer.data)
    if request.method=='PUT':
        item_instance=Item.objects.get(id=pk)
        serializer=ItemSerializer(item_instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method=='DELETE':
        item_instance=Item.objects.get(id=pk)
        item_instance.delete()
        return Response()
        
@api_view(['GET','PUT'])
def supplier(request, pk):
    if request.method=='GET':
        supplier_instance=Supplier.objects.get(id=pk)
        serializer=SupplierSerializer(supplier_instance)
        return Response(serializer.data)
    if request.method=='PUT':
        supplier_instance=Supplier.objects.get(id=pk)
        serializer=SupplierSerializer(supplier_instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET'])
def supplier_items(request, pk):
    serializer=ItemSerializer(Item.objects.filter(suppliers=pk), many=True)
    return Response(serializer.data)
        
        
