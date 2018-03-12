import requests
import xlwt
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    #确定来路网址
    'Cookie':'user_trace_token=20170609202938-2d01d3ccd0094005ad28c35ec0ffddcf; fromsite=www.zhihu.com; LGUID=20170609202939-4e58ec50-4d0f-11e7-9a2f-5254005c3644; ab_test_random_num=0; JSESSIONID=ABAAABAAAFCAAEG09A74105390C4D7EE760E1759FED3054; _putrc=D2EA0DEE8DB0F850; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B71675; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; TG-TRACK-CODE=index_message; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505897888,1506769562,1507107733,1507165069; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507165099; _gid=GA1.2.1551478845.1507107733; _ga=GA1.2.1490807978.1497011370; LGRID=20171005085822-48deff63-a968-11e7-ba1e-525400f775ce; SEARCH_ID=6acf1dbc506f4eee95635f92f3f8313b; index_location_city=%E5%8C%97%E4%BA%AC'
}

def getJobList(page):
    data = {
        'first': 'flase',
        'pn': page,
        'kd': 'python'
    }
    r = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0', data = data,headers = headers,timeout =30)#一个post请求
    result = r.json()
    jobs = result['content']['positionResult']['result']
    return jobs

excelTable = xlwt.Workbook()
sheet1 = excelTable.add_sheet('lagou',cell_overwrite_ok=True)

sheet1.write(0, 0, 'positionName')
sheet1.write(0, 1, 'salary')
sheet1.write(0, 2, 'workYear')
sheet1.write(0, 3, 'education')
sheet1.write(0, 4, 'jobNature')
sheet1.write(0, 5, 'city')
sheet1.write(0, 6, 'companyShortName')
sheet1.write(0, 7, 'district')
sheet1.write(0, 8, 'companySize')
sheet1.write(0, 9, 'companyFullName')

n = 1

for page in range(1,50):
    print(page)
    for job in getJobList(page=page):
        #print(job)
        sheet1.write(n,0,job['positionName'])
        sheet1.write(n, 1, job['salary'])
        sheet1.write(n, 2, job['workYear'])
        sheet1.write(n, 3, job['education'])
        sheet1.write(n, 4, job['jobNature'])
        sheet1.write(n, 5, job['city'])
        sheet1.write(n, 6, job['companyShortName'])
        sheet1.write(n, 7, job['district'])
        sheet1.write(n, 8, job['companySize'])
        sheet1.write(n, 9, job['companyFullName'])
        n += 1
        #time.sleep(2)

excelTable.save('lagou.xls')
