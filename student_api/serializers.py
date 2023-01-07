from rest_framework import serializers
from .models import Student, Path

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

    born_year = serializers.SerializerMethodField()
    path = serializers.StringRelatedField()  # to get data as a string version, read_only
    path_id = serializers.IntegerField()  # for create operation

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "number", "age", "born_year", "path", "path_id"]
        # exclude = ["age"]  cannot set both fields and exclude

    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()

        return current_time.year - int(obj.age)


class PathSerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = "detail"
    #     )  # many = True birden fazla student geleceği için

    students = StudentSerializer(many = True)

    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]