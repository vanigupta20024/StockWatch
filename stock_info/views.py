import json
from django.shortcuts import render
from django.http import HttpResponse
from jugaad_data.nse import NSELive

def stock_info(request, stock_name):
    data =  open('stock_info/static/stock_info/stock_data.json', 'r')
    json_data = json.loads(json.dumps(eval(data.read())))
    stock_name = json_data[stock_name]
    n = NSELive()
    ticks = []
    tick_data = n.tick_data(stock_name)['grapthData'][:]
    q = n.stock_quote(stock_name)
    price_info = q['priceInfo']
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
        "metadata" : metadata
    }
    return render(request, "stock_info/stock_info.html", data_object)