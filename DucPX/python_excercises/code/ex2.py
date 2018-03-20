import requests


SOURCE_URL = 'https://tuoitre.vn/tin-moi-nhat.htm'

def main():
    r = requests.get(SOURCE_URL)

    if r.ok:
        print("ok")
    else:
        print("Không thể truy cập được vào tuoitre.vn")

if __name__ == '__main__':
    main()
