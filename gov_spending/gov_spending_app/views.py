from django.shortcuts import render, redirect
from .config.remote import base_url
from .forms import fetch_form

# import request library
import requests


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    context = {'results' : '0'}
    # get api url
    if request.method == "POST":
        # fetch
        if 'button1' in request.POST:
            # get the form from the post request
            form = fetch_form(request.POST)
            # Validate the form
            if form.is_valid():
                api_url = base_url

                # make a get request to api endpoint
                response = requests.get(api_url)

                # response status 200: data has been received
                if response.status_code == 200:
                    # decode json response
                    content = response.json()
                    value = content['results']

                    # for the edge case of congressional_justification_url will be Null
                    # and JS cannot read
                    for i in range(len(value)):
                        if not value[i]['congressional_justification_url']:
                            value[i]['congressional_justification_url'] = 'None'

                    # send data response to template
                    context = {'results' : value}
        # withdraw
        elif 'button2' in request.POST:
            pass
    else:
        # passing empty form to the template
        context["form"] = fetch_form()
    return render(request, 'gov_spending_app/index.html', context)
