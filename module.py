from urllib import response

def get_web(url):
    '''URL을 매개 변수에 입력하면 내용을 반환하는 함수'''
    import  urllib.request
    response = urllib.request.urlopen(url) ## URL을 열고
    data = response.read() ## Data를 읽고
    decoded = data.decode('utf-8') ## 한글로 읽을 수 있게 Decoding
    return  decoded

url = input('웹 페이지의 URL 주소를 입력하세요>')
content = get_web(url)
print(content)