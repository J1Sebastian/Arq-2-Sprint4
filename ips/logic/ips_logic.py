from ips.models import Ips

def get_ipss():
    ipss = Ips.objects.all()
    return ipss

def get_ips(id):
    ips = Ips.objects.get(id=id)
    return ips