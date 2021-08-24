# 导入需要的库
import requests
import json
import re
import csv
# 宏变量存储目标js的URL列表
COMMENT_PAGE_URL = []


# 生成链接列表
def Get_Url(num):
    COMMENT_PAGE_URL.clear()
    # urlFront = 'https://rate.tmall.com/list_detail_rate.htm?itemId=10905215461&spuId=273210686&sellerId=525910381&order=3¤tPage='
    # urlRear = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvHQvRvpQvUpCkvvvvvjiPRLqp0jlbn2q96jD2PmPWsjn2RL5wQjnhn2cysjnhR86CvC8h98KKXvvveSQDj60x0foAKqytvpvhvvCvp86Cvvyv9PPQt9vvHI4rvpvEvUmkIb%2BvvvRCiQhvCvvvpZptvpvhvvCvpUyCvvOCvhE20WAivpvUvvCC8n5y6J0tvpvIvvCvpvvvvvvvvhZLvvvvtQvvBBWvvUhvvvCHhQvvv7QvvhZLvvvCfvyCvhAC03yXjNpfVE%2BffCuYiLUpVE6Fp%2B0xhCeOjLEc6aZtn1mAVAdZaXTAdXQaWg03%2B2e3rABCCahZ%2Bu0OJooy%2Bb8reEyaUExreEKKD5HavphvC9vhphvvvvGCvvpvvPMM3QhvCvmvphmCvpvZzPQvcrfNznswOiaftlSwvnQ%2B7e9%3D&needFold=0&_ksTS=1552466697082_2019&callback=jsonp2020'
    urlFront = 'https://rate.tmall.com/list_detail_rate.htm?itemId=616316315442&spuId=986750214&sellerId=4199378565&order=3&currentPage='
    urlRear = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvYQvEvbQvUpCkvvvvvjiWPFL9AjYRPsMwAjEUPmPh1jnbR2zU0jY8R2qwsjY8n8OCvvBvpvpZRvhvChCvvvvvvpvVph9vvvvvmvhvLhV%2B%2B9mFRAYVEvLvqbVQWlX9ZwsIRfU6pLEw9E7rVcOdNB3rsCkKfvxYVVzUVTtMoz3PlR9fVzxjfCuYiLUpwh%2BFp%2B0xhE36LFEc6a7IvpvUphvhqXTYIW8UvpvVpyUUCEQXKvhv8hCvvvvvvhCvphvwv9vvpkivpCQmvvChNhCvjvUvvhBZphvwv9vvBHpRvpvhMMGvvUOCvvBvppvv&needFold=0&_ksTS=1628824135157_430&callback=jsonp431'
    for i in range(0, num):
        COMMENT_PAGE_URL.append(urlFront + str(1 + i) + urlRear)



# 获取评论数据
def GetInfo(num):
    # 定义需要的字段
    nickname = []
    auctionSku = []
    ratecontent = []
    ratedate = []
    # 循环获取每一页评论
    for i in range(num):
        # 头文件，没有头文件会返回错误的js
        headers = {
            'cookie': 'cna=yMqPGcFTeTYCAXH4nmV+F16o; hng=CN%7Czh-CN%7CCNY%7C156; lid=zg5604; enc=Fe2bkMcXuhePiy%2Bf4qzLI%2FRBCQ%2BIeVJl0KSMkGsMfIOOVzYhrutZLh7U%2FJRkT99MvesD%2BL0MtKm2D9VjhdPTfg%3D%3D; sgcookie=E100asHEV%2B3ru89%2FV0PhIHD95iUUyOs6gIimp%2FZiZfE9ugqArsxN05lBI1mL9M7KQX%2B%2FDLiF4Qz6KondjqFF29LM9R44gvkVn6vHNxptRSJXf0w%3D; t=900ca7cfb0c5185c6f111ef32c8a0767; _tb_token_=5713e38b3eb3; cookie2=1a53bbcd0cd640f3cadb7d10115446a8; xlly_s=1; tfstk=cDzhBQgjNkoIM0ogcwgQTfbd1RjAZz8rnzz_7zH4fMXxdYaNiI-w0_ycsvfos31..; l=eBTxHyV7gTn7_2qhBOfwourza77OSIRAguPzaNbMiOCPO21H5xZ5W6HWrC8MC3GVh6RJR3PcCylgBeYBqnV0x6aNa6Fy_Ckmn; isg=BDIyapZnh1h6cLtjGBC65sLPg3gUwzZdVh13afwLXuXQj9KJ5FOGbTjpfysz_671',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'referer': 'https://detail.tmall.com/item.htm?id=616316315442&ali_refid=a3_430673_1006:1176030025:N:V8ZBjiQBpHQBA2kJB/sGSdPazk/YcJUkvk4H1TovH6s=:bd6dc7930b74dc6d68ec8e0963c1f04a&ali_trackid=1_bd6dc7930b74dc6d68ec8e0963c1f04a&spm=a2e0b.20350158.31919782.1',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
        }#伪装成浏览器访问，防止乱码或者防止访问失败
        # 解析JS文件内容
        print(COMMENT_PAGE_URL[i])
        content = requests.get(COMMENT_PAGE_URL[i], headers=headers).text  # 调用http接口并获取他的文字
        print(content)
        # nk = re.findall('"displayUserNick":"(.*?)"', content)
        # nickname.extend(nk)
        # # print(nk)
        nickname.extend(re.findall('"displayUserNick":"(.*?)"', content))  # 正则表达式匹配存入列表
        auctionSku.extend(re.findall('"auctionSku":"(.*?)"', content))
        ratecontent.extend(re.findall('"rateContent":"(.*?)"', content))
        ratedate.extend(re.findall('"rateDate":"(.*?)"', content))
    # 将数据写入TEXT文件中
    for i in list(range(0, len(nickname))):
        text = ','.join((nickname[i], ratedate[i], auctionSku[i], ratecontent[i])) + '\n'
        print(i + 1,text)
        with open(r"TmallContent2.csv", 'w', encoding='UTF-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([nickname[i],ratedate[i],ratecontent[i]])
            print(i + 1, ":写入成功")


# 主函数
if __name__ == "__main__":
    Page_Num = 10
    Get_Url(Page_Num)
    GetInfo(10)