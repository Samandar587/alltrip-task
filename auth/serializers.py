from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)

        def validate(self, attrs):
                
            username = attrs.get('username')
            password = attrs.get('password')

            if username and password:
                  
                  user = authenticate(request=self.context.get('request'), username=username, password=password)

                  if not user:
                        msg = "Access denied: wrong username or password"

                        raise serializers.ValidationError(msg, code='authorization')
                  
            else:
                  msg = 'Both username and password are required'
                  raise serializers.ValidationError(msg, code='authorization')
            
            attrs['user'] = user
            return attrs
