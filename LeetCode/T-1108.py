class Solution:
    def defangIPaddr(self, address):
        addr = address.split('.')
        for i in range(1, len(addr) + 2, 2):
            addr.insert(i, '[.]')

        return ''.join(addr)


if __name__ == '__main__':
    address = "1.1.1.1"
    s = Solution()
    print(s.defangIPaddr(address))
