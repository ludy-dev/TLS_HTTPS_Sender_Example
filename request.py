from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl, requests

class adapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
           num_pools=connections,
           maxsize=maxsize,
           block=block,
           ssl_version=ssl.PROTOCOL_TLSv1_2
        )
        print('init poolmanage')
def request_https():
    with requests.Session() as s:
        s.mount('https://', Adapter())
        r = s.get('https://google.com', verify=False)
        print(r.text)

if __name__ == '__main__':

    request_https()


