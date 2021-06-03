import json
from django.shortcuts import render
    
def listing(request):
    with open(r'static\updated_data.json', 'r') as file:
        json_data = json.load(file)
        upper_list = json_data['upper']
        losers = json_data['loss']
        gainers = json_data['gain']
        search_input = json_data['search_input']
    return render(request, 'listing/listing.html', {"upper" : upper_list, "loss" : losers, "gain" : gainers, 'search_input':search_input})
    