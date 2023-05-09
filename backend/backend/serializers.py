from rest_framework import serializers
from .models import Document, Annotation

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['start', 'end', 'label', 'text', 'document']

class DocumentSerializer(serializers.ModelSerializer):
    annotations = AnnotationSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['document', 'annotations', 'id']

    def create(self, validated_data):
        document = Document.objects.create(**validated_data)
        return {'id': document.id}

    def to_representation(self, instance):
        action = self.context['view'].action
        if action == 'create':
            return super().to_representation({'id': instance['id']})
        elif action == 'retrieve':
            data = super().to_representation(instance)
            del data['id']
            return data
        else:
            return super().to_representation(instance)