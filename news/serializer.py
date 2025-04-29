from rest_framework import serializers 
from .models import NewsThree 


class NewsThreeSerializers(serializers.ModelSerializers): 
    class Meta:
        model = NewsThree
        fields = ['id', 'title', 'description', 'image']
    