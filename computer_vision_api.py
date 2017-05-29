import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

api_f = open('apikey.json', 'r')
keys = json.load(api_f)
api_f.close()

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': keys["key1"]
}

params = urllib.parse.urlencode({
    'visualFeatures': 'Tags',
    'details': 'Celebrities',
    'language': 'en',
})

try:
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    f = open('response/result.txt', 'a')
    img_f = open('images/path.txt', 'r')
    lines = img_f.readlines()
    for image_path in lines:
        body = "{'url':'" + image_path + "'}"
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        if response.status == 200:
            f.write(str(data, 'utf-8') + '\n')
    conn.close()
    img_f.close()
    f.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

