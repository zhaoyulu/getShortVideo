import requests
import json
import codecs

# 文件路径
path = '/media/'
num = 0


def response(flow):
    global num
    # 经测试发现视频url前缀主要是3个
    target_urls2 = ['https://api.amemv.com']
    # 设置视频名
    for url in target_urls2 :
        if flow.request.url.startswith(url):
            response = flow.response
            data = response.content
            quiz = json.loads(data)
            #print(quiz['aweme_list'][0])
            quiz['aweme_list']
            filename = path + str(num) + '.txt'
            #for temp in quiz['aweme_list']:
            save(filename,json.dumps(quiz))
            print(filename + '下载完成')

            print(flow.request.url)

            #with open(filename, 'ab') as f:
                #f.write(res.content)
                #f.flush()
                #print(filename + '下载完成')
            num += 1
                        #print(filename + '下载完成')
            #print("URL:是")
            #print(flow.request.url)

def save(filename, contents):
        fh = open(filename, 'w', encoding='utf-8')
        fh.write(contents)
        fh.close()
