import subprocess
import optparse
import re



def get_inputs():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface daxil edilir")
    parser.add_option("-m","--mac_address",dest="mac_address",help="Mac_addres daxil edilir")
    return parser.parse_args()

def control_inputs(interface,mac_address):
    if not interface:
        interface=input("Interface daxil edin::")
    if not mac_address:
        mac_address=input("Mac_addressi daxil edin:: ")
    return interface,mac_address

def control_macchanger(interface,mac_address):
    print("basladi...")

    subprocess.check_call(["ifconfig", interface, "down"])
    subprocess.check_call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.check_call(["ifconfig", interface, "up"])


def check_mac(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    ifconfig_str=ifconfig.decode()
    new_mac=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        return False


print(""""
  __  __               _____ _                                 
 |  \/  |             / ____| |                                
 | \  / | __ _  ___  | |    | |__   __ _ _ __   __ _  ___ _ __ 
 | |\/| |/ _` |/ __| | |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |  | | (_| | (__  | |____| | | | (_| | | | | (_| |  __/ |   
 |_|  |_|\__,_|\___|  \_____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                                __/ |          
                                               |___/               by Bahram Aghaahmedli

""")
interface=""
mac_address=""
(user_inpputs,args)=get_inputs()
interface,mac_address=control_inputs(user_inpputs.interface,user_inpputs.mac_address)
control_macchanger(interface,mac_address)
Final_mac=check_mac(interface)
if Final_mac==mac_address:
    print("Mac adres ugurla deyisdirildi")
else:
    print("Xeta bas verdi")

