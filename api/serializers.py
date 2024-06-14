from rest_framework import serializers
from .models import Item, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True)
    
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        try:    
            suppliers_data = validated_data.pop('suppliers')
            item = Item.objects.create(**validated_data)
            item.suppliers.set(suppliers_data)

            return item
        except Exception as e:
            print(f"message:{e}")


    def update(self, instance, validated_data):
        suppliers_data = validated_data.pop('suppliers', [])
        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.save()

        instance.suppliers.set(suppliers_data)
        return instance
