import network
import net_cfg
import time

wlan = network.WLAN(network.STA_IF)


def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network: {}...'.format(net_cfg.SSID))
        wlan.connect(net_cfg.SSID, net_cfg.PASS)
        attempt = 0
        while not wlan.isconnected() and attempt < 5:
            print("Attempt {}/5".format(attempt + 1))
            time.sleep(3)
            attempt += 1
        if attempt >= 5:
            print(
                ("Failed to connect to network {}. Check settings in "
                 + "net_cfg.py").format(net_cfg.SSID)
            )
            wlan.disconnect()
            return
    conn_config = wlan.ifconfig()
    print('\nNetwork config:')
    print("IP address: {}".format(conn_config[0]))
    print("Subnet Mask: {}".format(conn_config[1]))
    print("Gateway: {}".format(conn_config[2]))
    print("DNS Server(s): {}\n".format(conn_config[3]))


def get_ipaddress():
    return wlan.ifconfig()[0]


def is_connected():
    return wlan.isconnected()