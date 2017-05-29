import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

f = open('apikey.json', 'r')
keys = json.load(f)

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': keys["key1"]
}

params = urllib.parse.urlencode({
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
})

body = "{'url':'http://shop.r10s.jp/book/cabinet/5652/9784065095652.jpg'}"

try:
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

