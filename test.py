python3 manage.py shell

from web.models import People, CloudServiceTypes, ConnectingPoints, FicConnectionBandwidths

connecting_point = ConnectingPoints.objects.filter(id=1).first()
fic_bandwidth = FicConnectionBandwidths.objects.all()
print(fic_bandwidth)

for fb in fic_bandwidth.iterator():
    connecting_point.available_bandwidths.add(fb)
    connecting_point.updatable_bandwidths.add(fb)



python3 manage.py shell

from web.models import People, CloudServiceTypes, ConnectingPoints, FicConnectionBandwidths

connecting_point = ConnectingPoints.objects.filter(id=2).first()
fic_bandwidth = FicConnectionBandwidths.objects.all()
print(fic_bandwidth)

for fb in fic_bandwidth.iterator():
    connecting_point.available_bandwidths.add(fb)
    connecting_point.updatable_bandwidths.add(fb)