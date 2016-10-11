from tastypie.resources import ModelResource
from orderapi.orderbase.models import Users, Merchandise, Order, OrderDetails

class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'users'

class MerchResource(ModelResource):
    class Meta:
        queryset = Merchandise.objects.all()
        resource_name = 'merch'



