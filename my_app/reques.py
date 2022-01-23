import json
def sendResJson(data, msj, code):
       
    return json.dumps(
    {
        'code': code,
        'data':data
    }
    ),code