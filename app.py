from flask import Flask
from flask import request
from flask import jsonify
import google_utils as gutil
import time
cache = gutil.cache_machine.load_data()
app = Flask(__name__)

def parse_query(q):
    #q = json.loads(request.data)['q']
    args = q.split(' ')
    results = []
    is_image = False
    for i in args:
        if 'image_name:' == i:
            is_image = True
        if ':' in i:
            args.remove(i)

    for i in cache:
        append = True
        for j in args:
            if str(j) in str(i):
                continue
            else:
                append = False
                break
        if append:
            results.append(i)

    if is_image:
        return gutil.images.get_picture(results[0][1])
    else:
        return results

if __name__ == "__main__":
    q = "family: Bovidae Tribe: Alcelaphini Origin: NMB"
    res = parse_query(q)
    for i in res:
        print("Family: " + str(i[7]) + " Tribe: " + str(i[8]) + " Origin: " + str(i[2]))
    q2 = "image_name: DSCN4819"
    res = parse_query(q2)
    print(res)
