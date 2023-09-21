from django.shortcuts import render
from Productapp.serializers import CategorySerializer, ProductSerializer
import rest_framework
import rest_framework.generics
import rest_framework.permissions
from Productapp.models import CategoryModel, ProductModel
from groceryBackend.Globalimport import*

# Create your views here.
class CategoryView(ListAPIView):
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        try:
            qs = CategoryModel.objects.all()
            id = self.request.GET.get('id')
            if id:qs = qs.filter(id=id)
            return qs
        except:return None
    def post(self,request):
        try:
            try : id= self.request.data['id']
            except : id = ''
            if id:
                category_qs = CategoryModel.objects.filter(id=id)
                if category_qs.count():
                    category_qs = category_qs.first()
                else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No recordfound with given id"})
                category_obj = CategorySerializer(category_qs,data = self.request.data,partial=True)
                category_obj.is_valid(raise_exception=True)
                msg = "Updated Successfully"
                
            else:
                category_obj = CategorySerializer(data = self.request.data,partial=True)
                category_obj.is_valid(raise_exception=True)
                msg = "Created Successfully"
            return Response({"status":status.HTTP_200_OK,"message":msg})
        except Exception as e:return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            if id:
                obj = CategoryModel.object.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"status":status.HTTP_200_OK,"message":"Deleted Successfully"})
                else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No record found with given id"})
            else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"id not found"})
        except Exception as e:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
            
class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        try:
            qs = ProductModel.objects.all()
            id = self.request.GET.get('id')
            if id:qs = qs.filter(id=id)
            return qs
        except:return None
    def post(self,request):
        try:
            try : id= self.request.data['id']
            except : id = ''
            if id:
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No recordfound with given id"})
                product_obj = ProductSerializer(product_qs,data = self.request.data,partial=True)
                product_obj.is_valid(raise_exception=True)
                msg = "Updated Successfully"
                
            else:
                product_obj = ProductSerializer(data = self.request.data,partial=True)
                product_obj.is_valid(raise_exception=True)
                msg = "Created Successfully"
            return Response({"status":status.HTTP_200_OK,"message":msg})
        except Exception as e:return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            if id:
                obj = ProductModel.object.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"status":status.HTTP_200_OK,"message":"Deleted Successfully"})
                else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No record found with given id"})
            else:return Response({"status":status.HTTP_404_NOT_FOUND,"message":"id not found"})
        except Exception as e:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":str(e)})
            