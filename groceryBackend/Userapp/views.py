from Userapp.serializers import userSerializer
from Userapp.models import UserModel
from groceryBackend.validation import validate
from groceryBackend.Globalimport import*
from django.contrib.auth.hashers import make_password

# Create your views here.
class Userview(ListAPIView):
    serializer_class = userSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get_queryset(self):
        try:
            superuser = self.request.user.is_superuser
            id = self.request.Get.get('id')
            qs = UserModel.objects.all()
            if id:qs = qs.filter(id=id)
            if superuser : qs =qs
            return qs 
        except:return None
    def post(self,request):
        user_obj =''
        try:id = self.request.GET.get('id')
        except: id = ''
        try: contact = self.request.data['contact']
        except:contact=''
        try: username = self.request.data['username']
        except:username=''
        try: password = self.request.data['password']
        except:password=''
        try:
            mandatory = ["username","password"]
            data = validate(self.request.data,mandatory)
            if id:
                try:
                    user = UserModel.objects.all()
                    if user.count():
                        user = user.first()
                    else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No user found with given id"})
                    serializer = userSerializer(user,data=request.data,partial=True)
                    serializer.is_valid(raise_exception=True)
                    if password:
                        msg = "User detail and Password Updated Successfully"
                        user_obj=serializer.save(password = make_password(password))
                    else: 
                        msg = "User details updated successfully"
                        user_obj = serializer.save()
                except Exception as e:
                    if user_obj:user_obj.delete()
                    else:pass
                    return Response({"status":status.HTTP_400_BAD_REQUEST,"message":f"Excepction occured {e}"})            
            else:
                if data==True:
                    try: 
                        serializer = userSerializer(data=request.data,partial=True)
                        serializer.is_valid(raise_exception=True)
                        msg = "Created New User"
                        user_obj = serializer.save(password=make_password(self.request.data['password']))
                        return Response({"status":status.HTTP_200_OK,"message":msg})
                    except Exception as e :
                        return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
                else: return Response({"status":status.HTTP_404_NOT_FOUND,"message":data})
        except Exception as e : 
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
    def delete(self,request):
        id = self.request.data['id']
        user_obj = UserModel.objects.filter(id=id)
        if user_obj.count():
            user_obj.delete()
            return Response({"status":status.HTTP_200_OK,"message":"Deleted Successfully"})
        else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No record Found With given id"})

class LoginView(ObtainAuthToken):
    def post(self,request , *args , **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        try:
            test = serializer.is_valid(raise_exception=True) 
            user = serializer.validated_data['user']

            
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "status":status.HTTP_200_OK,
                "token":"Token"+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            # print("e",e)
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Incorrect Username or Password",
                "excepction":str(e),
            })
class Logout(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
  
    def get(self,request):
        try:
            Data = Token.objects.get(user = self.request.user.id)
            Data.delete()
            # print("ok")
            return Response({"status":status.HTTP_200_OK,"message":"logout successfully"})
        except Exception as e:
            # print("e",e)
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})