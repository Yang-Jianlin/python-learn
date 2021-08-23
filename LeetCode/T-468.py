class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ':' in IP:
            ip_list = IP.split(':', 7)
            if len(ip_list) != 8:
                return "Neither"
            for i in ip_list:
                try:
                    if len(i) > 4 or len(i) <= 0:
                        return "Neither"
                    elif int(i, 16) < 0 or int(i, 16) > 65535:
                        return "Neither"
                except Exception:
                    return "Neither"
            return 'IPv6'
        else:
            ip_list = IP.split('.', 3)
            if len(ip_list) != 4:
                return "Neither"
            for i in ip_list:
                try:
                    n = list(i)
                    if len(i) > 3 or len(i) <= 0:
                        return "Neither"
                    elif len(n) != 1 and n[0] == '0':
                        return "Neither"
                    elif int(i) < 0 or int(i) > 255:
                        return "Neither"
                except Exception:
                    return "Neither"
            return 'IPv4'


if __name__ == '__main__':
    IP = "192.0.0.1"
    s = Solution()
    print(s.validIPAddress(IP))
