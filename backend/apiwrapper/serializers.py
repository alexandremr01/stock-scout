import json

# json to json
def alphav_to_ss(alphav_data, freq):
    alphav = {
        'DAY': 'Time Series (Daily)',
        'WEEK': 'Weekly Adjusted Time Series',
        'MONTH': 'Monthly Adjusted Time Series'
    }

    ss_arr = []
    time_series = alphav_data[alphav[freq]]
    for key, value in time_series.items():
        ss_dict = {
            'Date': key,
            'open': value['1. open'],
            'close': value['4. close']
        }
        ss_arr.append(ss_dict)
    
    return json.loads(json.dumps(ss_arr))
