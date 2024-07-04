from rest_framework import serializers
from home.models import person,Team
from django.contrib.auth.models import User

class RegisterSerializer(serializers.serializer)
    username=serializers.CharField()
    email=serializers.EmailField()
    Password=serializers.CharField()
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.validationError("Username already exists")
            if data['email']:
                if User.objects.filter(email=data['email']).exists()
                raise serializers.validationError("Email alredy exists")
            return data

    

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class Loginserializer(serializers.serializer)
    username=serializers.CharField()
    password=serializers.CharField()



class Teamserializer(serializers.Modelserializer)
    class Meta:
        model=Team
        field=['team_name']

class personserializer(serializers.Modelserializer):
    team=Teamserializer()
    team_info=serializers.serializerMethodField()
    class Meta:
        model=person
        field='__all__'
        depth=1

    def get_team_info(self,obj):
        return "extra serialize field"
    
        
    def validate(self,data):
        spl_chars ="!@#$%^&*()_+,<>/"

        if any(c in spl_chars for c in data['name']):
            raise serializers.validationError("name should not have special character")

        if data['age']<18:
            raise serializers.validationError("age should not be less than 18")

        return data    