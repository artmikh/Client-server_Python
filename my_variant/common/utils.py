import json

def get_data_from_message(data):
    d_data = data.decode('utf-8')
    d = json.loads(d_data)
    return d
    
def send_message(file, field, *args):
    with open(file, 'r', encoding='utf-8') as f_n:
        data = json.load(f_n)[field]
        str_data = json.dumps(data)

        return str_data