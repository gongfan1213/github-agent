import os
for k in ['HTTP_PROXY', 'http_proxy', 'HTTPS_PROXY', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    if k in os.environ:
        print(f"删除环境变量: {k}")
        del os.environ[k]

import requests
print("开始请求 https://api.github.com ...")
r = requests.get("https://api.github.com", proxies={})
print(r.status_code)
print(r.text)