from django.shortcuts import render
import os
import pprint

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.middleware.csrf import get_token
from django_common.http import JsonResponse
from neighborhood.models import Neighborhood
from neighborhood.forms import NeighborhoodForm
from slacker import Slacker

def neighborhood_list(request, template='neighborhood/list.html'):
    client = Slacker(os.environ['SLACK_API_ACCESS_TOKEN'])
    channels = client.channels.list()
    team_info = client.team.info().body
    data = {
        'channels': channels.body,
        'team_info': team_info
    }

    return render(request, template, data)

from neighborhood.forms import NeighborhoodForm
def neighborhood_details(request, id, template='neighborhood/details.html'):
    d = {}
    item = get_object_or_404(Neighborhood, pk=id)
    d['form'] = NeighborhoodForm(instance=item)
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'form': NeighborhoodForm(instance=item).as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['neighborhood'] = Neighborhood.objects.get(pk=id)
    return render(request, template, d)

def neighborhood_delete(request, id):
    item = Neighborhood.objects.get(pk=id)
    item.delete()
    return JsonResponse()
