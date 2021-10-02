book = {}
book["Tom"]={"name":"Tom", "address":"Thalias 345", "phone": 1039284}
book["George"]={"name":"George", "address":"Euelpis 756", "phone": 5341545454}

import json

s = json.dumps(book)
print(s)

