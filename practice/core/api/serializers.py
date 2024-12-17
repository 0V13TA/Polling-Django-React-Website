from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Product
        fields = ["title", "content", "price", "sale_price", "my_discount"]

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, models.Product):
            return None
        return obj.get_discount()
