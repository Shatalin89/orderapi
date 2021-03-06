from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from orderapi.orderbase.models import Merchandise


# Create your views here.

def index(request):
    latest_merch_list = Merchandise.objects.order_by('-name_merch')[:5]
    template = loader.get_template('order/index.html')
    context = RequestContext(request, {'latest_merch_list': latest_merch_list,})
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def upload_photo(request):                                                                                  
    if request.method=='POST':
        image = request.FILES['image']                                                                              title1 =''                                                                                                  new_image = Photo(title=title1,photo=image,description='')                                                  new_image.save()                                                                                            response_data=[{"success": "1"}]                                                                            return HttpResponse(simplejson.dumps(response_data), mimetype='application/json') 
