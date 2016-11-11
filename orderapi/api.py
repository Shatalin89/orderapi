from tastypie.resources import ModelResource, ALL
from orderapi.orderbase.models import UsersOrder, Merchandise, Order, OrderDetails
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from django.db.models import signals
from tastypie.models import create_api_key



signals.post_save.connect(create_api_key, sender=User)

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
    class Meta:
        queryset = Merchandise.objects.all()
        resource_name = 'merch'
        allowed_methods = ['get', 'post']
      #  authentication = ApiKeyAuthentication()
        authorization = Authorization()
 #       filtering = {
  #          'username': ALL,
   #     }


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
   #     authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
    #    authorization = DjangoAuthorization()

class OrderDetailsResource(ModelResource):
    class Meta:
        queryset = OrderDetails.objects.all()
        resource_name = 'ordetails'
    #    authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
     #   authorization = DjangoAuthorization()
 


