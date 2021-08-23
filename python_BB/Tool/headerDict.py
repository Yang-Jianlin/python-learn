def header_dict(raw_headers):
    headers = dict([line.split(": ", 1) for line in raw_headers.split("\n")])

    return headers


if __name__ == '__main__':
    raw_headers = """cname: 
pid: 
keyword: 秦皇岛
pageIndex: 1
pageSize: 10"""
    print(header_dict(raw_headers))
