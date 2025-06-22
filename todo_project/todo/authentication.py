from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        print("login request recieved")
        response=super().post(request,*args, **kwargs)
        print("response from super")
        
        token=Token.objects.get(key=response.data.get("token"))
        return Response({
            'token':token.key,
            'user_id':token.user_id,
            'username':token.user.username,
        })