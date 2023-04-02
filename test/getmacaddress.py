from getmac import get_mac_address
import ipaddress
# eth_mac = get_mac_address(interface="eth0")
# win_mac = get_mac_address(interface="Ethernet")
# ip_mac = get_mac_address(ip="192.168.0.1")
# ip6_mac = get_mac_address(ip6="::1")
# host_mac = get_mac_address(hostname="localhost")
# updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)

# print(host_mac)


# Enable debugging
# from getmac import getmac
# getmac.DEBUG = 2  # DEBUG level 2
#print(getmac.get_mac_address())
#mac = get_mac_address(interface="Ethernet")
import getmac
getmac.DEBUG = 2

# for x in range(100,200):
#     mac = getmac.get_mac_address()
#     print(mac)


# # Change the UDP port used for updating the ARP table (UDP packet)
# from getmac import getmac
# getmac.PORT = 44444  # Default is 55555
# print(getmac.get_mac_address(ip="192.168.0.1", network_request=True))
try:
    a = 10
    a = float(a)
    print(a)
except Exception as e:
    print(e)
