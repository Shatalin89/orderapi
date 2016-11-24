from tastypie.resources import ModelResource, ALL
from orderapi.orderbase.models import UsersOrder, Merchandise, Order, OrderDetails
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from django.db.models import signals
from tastypie.models import create_api_key



signals.post_save.connect(create_api_key, sender=User)


class MultiPartResource(object):
   def deserialize(self, request, data, format=None):
       if not format:
           format = request.Meta.get('CONTENT_TYPE', 'application/json')
       if format == 'application/x-www-form-urlencoded':
           return request.PUT
       if format.startswith('multipart'):
           data = request.PUT.copy()
           data.update(request.FILES)
           return data
       return super(MultiPartResource, self).deserialize(request, data, format)



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
#        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
#        authorization = DjangoAuthorization()


class UsersOrderResource(ModelResource):
    class Meta:
        queryset = UsersOrder.objects.all()
        resource_name = 'usersorder'
 #       authentication = BasicAuthentication()
  #      authorization = DjangoAuthorization()       

class MerchResource(ModelResource):
#    image = Merchandise.ImageField(attribute="image", null=True, blank=True)
    class Meta:
        queryset = Merchandise.objects.all()
        resource_name = 'merch'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()
   

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
   #     authentication = Multiuthentication(BasicAuthentication(), ApiKeyAuthentication())
    #    authorization = DjangoAuthorization()

class OrderDetailsResource(ModelResource):
    class Meta:
        queryset = OrderDetails.objects.all()
        resource_name = 'ordetails'
    #    authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
     #   authorization = DjangoAuthorization()
 


