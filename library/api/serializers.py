from rest_framework import serializers
from lib_base_model.models import Book, Publisher

#class PublisherSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(max_length=32, required=True)
    
    #def create(self, validated_data):
        #return Publisher.objects.create(**validated_data)
    
    #def update(self, instance, validated_data):
        #instance.name = validated_data.get("name")
        #instance.save()
        #return instance
    

#class BookSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(max_length=64, required=True)
    #ISBN = serializers.CharField(max_length=20, required=True)
    #summary = serializers.TextField(required=False)
    #publisher = serializers.PublisherSerializer()
    
    #def create(self, validated_data):
        #b = Book()
        #b.name = validated_data.get("name")
        #b.ISBN = validated_data.get("ISBN")
        #b.summary = validated_data.get("summary")
        #b.publisher = validated_data.get("publisher")
        #b.save()
        #return b
    
    #def update(self, instance, validated_data):
        
        #pass

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name')

class BookSerializer(serializers.ModelSerializer):
    
    publisher_id = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects, source="publisher")
    
    publisher= PublisherSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ('id', 'name', 'ISBN', 'summary', 'publisher_id', 'publisher')

