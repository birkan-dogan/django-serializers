from rest_framework import serializers
from .models import Student

# serializer yazarken kullanabileceğimiz 1. yöntem ama kullanışlı değil
"""
class StudentSerializer(serializers.Serializer):
    # buraya hangi tabloyu serialize edeceksek onun field'larını getirmeliyiz
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    number = serializers.IntegerField()
    age = serializers.IntegerField()


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
"""

# serializer yazarken kullanacağımız yöntem

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["age"]  cannot set both fields and exclude
