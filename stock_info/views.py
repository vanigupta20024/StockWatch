import json
from django.shortcuts import render
from django.http import HttpResponse
from jugaad_data.nse import NSELive

def stock_info(request, stock_name):
    if "search" in request.GET:
        print(request.GET['data'])
    path = 'stock_info/static/stock_info/stock_data.json'
    with open('static/updated_data.json', 'r') as file:
        json_data = json.load(file)
        search_input = json_data['search_input']
    with open(path, 'r') as j:
        json_data = json.loads(j.read())
    stock_name = json_data[stock_name]
    n = NSELive()
    ticks = []
    tick_data = n.tick_data(stock_name)['grapthData'][:]
    q = n.stock_quote(stock_name)
    price_info = q['priceInfo']
    price_info['pChange'] = float(str(price_info['pChange'])[:6])
    price_info['change'] = float(str(price_info['change'])[:6])
    metadata = q['metadata']
    security_info = q['securityInfo']
    info = q['info']

    for i in tick_data:
        ticks.append(i[1])
    
    data_object = {
        "ticks" : ticks,
        "name" : stock_name,
        "price_info" : price_info,
        "info" : info,
        "security_info" : security_info,
        "metadata" : metadata,
        "search_input" : search_input
    }
    return render(request, "stock_info/stock_info.html", data_object)