import json
import yfinance as yf
from jugaad_data.nse import NSELive
from nsetools import Nse

def metadata_json():
    nse = NSELive()
    all_indices = nse.all_indices()
    nse_past = Nse()

    # Nse data - nifty bank
    nse_info = {}
    nse_info['name'] = all_indices['data'][13]['index']
    nse_info['market'] = 'NSE'
    nse_info['change'] = all_indices['data'][13]['variation']
    nse_info['lastPrice'] = str(all_indices['data'][13]['last'])
    nse_info['pChange'] = str(all_indices['data'][13]['percentChange'])
    if float(nse_info['change']) > 0:
        nse_info['change'] = "+" + str(nse_info['change'])
    else: nse_info['change'] = str(nse_info['change'])

    # Nse data - nse_50
    nse_50 = {}
    nse_50['name'] = all_indices['data'][0]['index']
    nse_50['market'] = 'NSE'
    nse_50['change'] = all_indices['data'][0]['variation']
    nse_50['lastPrice'] = str(all_indices['data'][0]['last'])
    nse_50['pChange'] = str(all_indices['data'][0]['percentChange'])
    if float(nse_info['change']) > 0:
        nse_50['change'] = "+" + str(nse_50['change'])
    else: nse_50['change'] = str(nse_50['change'])

    # Bse data
    current_bse = yf.Ticker("^BSESN").info
    bse_lastPrice = current_bse['regularMarketPrice']
    bse_previousClose = current_bse['regularMarketPreviousClose']
    bse_change = bse_lastPrice - bse_previousClose
    bse_pChange = (abs(bse_change) / bse_lastPrice) * 100
    if float(bse_change) > 0: bse_change = '+' + str(bse_change)
    if float(bse_change) < 0: bse_pChange = '-' + str(bse_pChange)
    bse_info = {
        'name' : 'SENSEX', 'market' : 'BSE',
        'lastPrice' : str(bse_lastPrice),
        'change' : str(bse_change)[:6],
        'pChange' : str(bse_pChange)[:6]
    }

    top_losers = nse_past.get_top_losers()
    top_gainers = nse_past.get_top_gainers()

    def add_data(source):
        data = []
        for i in source:
            temp = []
            temp.append(f'<a href="stock_info/{i["symbol"]}" target="_blank">{i["symbol"]}</a>')
            temp.append(i['ltp'])
            temp.append(i['highPrice'])
            temp.append(i['lowPrice'])
            temp.append(i['openPrice'])
            temp.append(i['previousPrice'])
            data.append(temp)
        return data

    upper_list = {
        'bse' : bse_info, 
        'nse' : nse_50, 
        'nif': nse_info,
    }

    losers = json.dumps(add_data(top_losers))
    gainers = json.dumps(add_data(top_gainers))
    s_input =  open(r'listing\static\listing\stock_data_list.json', 'r')
    search_input = json.dumps(eval(s_input.read()))

    data = {
        'upper': upper_list,
        'loss': losers,
        'gain': gainers,
        'search_input': search_input
    }

    with open(r'static\updated_data.json', 'w') as outfile:
        json.dump(data, outfile)