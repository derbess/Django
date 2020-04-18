from rest_framework import serializers

from mid.main.models import Book, Journal



class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    num_pages = serializers.IntegerField(read_only=True)
    # price = serializers.IntegerField(read_only=True)
    # description = serializers.CharField(read_only=True)
    # created_at = serializers.DateField(read_only=True)
    # genre = serializers.CharField(read_only=True)

    # email = serializers.EmailField()

    # def create(self, validated_data):
    #     created new instance
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     return instance

    class Meta:
        model = Book
        fields = ('id', 'name', 'num_pages', 'genre')

    def validate_name(self, value):
        if value<=0:
            raise serializers.ValidationError('invalid number of pages')
        return value

    def validate(self, attrs):
        # check object level validation,
        # if any raise serializer.ValidationError
        return attrs


class JournalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    type = serializers.IntegerField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateField()
    publisher = serializers.CharField()

    # email = serializers.EmailField()

    # def create(self, validated_data):
    #     created new instance
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     return instance

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'description', 'type', 'publisher')

    def validate_type(self, value):
        if (value != 1 or value!=2 or value!=3 or value!=4):
            raise serializers.ValidationError('invalid type')
        return value

