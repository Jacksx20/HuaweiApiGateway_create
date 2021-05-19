# coding: utf-8

from apig_sdk import signer
import requests
from openstack import connection


projectId = "092e2a9c6e00f38d2f1ec009d5112a0f"
cloud = "myhuaweicloud.com"
region = "cn-north-4"    # example: region = "cn-north-1"
AK = "DMA2IKDTP9XOW81YYQYB"
SK = "8ouVwMWR3iv1rKfe6dShPoSpwGOw8kXvyA5XpCzX"

conn = connection.Connection(
              project_id=projectId,
              cloud=cloud,
              region=region,
              ak=AK,
              sk=SK)


def test_compute():
    servers = conn.compute.servers(limit=3)
    for server in servers:
        print(server)


if __name__ == "__main__":
    test_compute()

    sig = signer.Signer()
    sig.Key = "***********"
    sig.Secret = "******"

    body = {
        "os-change": {
            "keyname": "***************",
            "userid": "***************",
            "imageid": "*****************",
            "mode": "withStopServer"
        }
    }

    r = signer.HttpRequest("POST",
                           "*******************************",
                           {"x-stage": "RELEASE"},
                           body)
    sig.Sign(r)

    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
    print(resp.status_code, resp.reason)
    print(resp.content)

