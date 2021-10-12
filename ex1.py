from sys import argv

def calc_zp(ihours, iprice, iaddpayment):
    return ihours * iprice + iaddpayment


if __name__ == '__main__':
    ihours, iprice, iaddpayment = argv[1:4]
    print(calc_zp(int(ihours), int(iprice), int(iaddpayment)))
