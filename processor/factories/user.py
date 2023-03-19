from django.contrib.auth.models import User
from processor.serializers.user import UserSerializer

class UserRegister:

    def validate(self, msg):
        serializer = UserSerializer(data=msg)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def process(self, msg):
        data = self.validate(msg)
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        return True

    # Handle duplicate user