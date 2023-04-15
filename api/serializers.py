from rest_framework import serializers
from tryapi.models import Blogpost

class BlogpostSerializer2(serializers.ModelSerializer):
    many_post = serializers.SerializerMethodField('get_many_post')
    x = 0
    def get_many_post(self, post):
        self.x = self.x + 1
        return self.x
    
    class Meta:
        model = Blogpost
        fields = ['id','title', 'description', 'created_at', 'many_post']

class BlogpostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blogpost
        fields = '__all__'