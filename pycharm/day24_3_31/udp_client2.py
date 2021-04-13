import socket


def client(ipaddr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置初始的客户端等待响应时间
    delay = 0.1
    while True:
        send_data = input('enter info:')
        s.sendto(send_data.encode(), (ipaddr, port))
        print('waiting up to {0} seconds for a reply'.format(delay))
        s.settimeout(delay)
        try:
            data, addr = s.recvfrom(1024)
            print('From {0} Data:{1}'.format(addr, data.decode()))
            if data:
                delay = 0.1
        except socket.timeout:
            # 每次超时后，需要动态调整等待时间，当等待时间大于2秒时，就认为服务端宕机
            delay *= 2
            if delay > 2.0:
                print('Server down')
                break
            else:
                continue


if __name__ == '__main__':
    client('127.0.0.1', 12345)
