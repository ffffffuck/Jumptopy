import urllib.request
import datetime
import json
import math

access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))


#[CODE 1]
def getTourPointVisitor(edCd):

    end_point='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?_type=json&serviceKey="+access_key
    parameters += "&YM="+'201612'
    parameters += '&ED_CD='+edCd

    url=end_point+parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 2]
#
# def getTourPointData(item,yyyymm,jsonResult):
#
#     natCd = 0 if 'natCd' not in item.keys() else item['natCd']
#     natKorNm = '' if 'natKorNm' not in item.keys() else item['natKorNm']
#     num = 0 if 'num'not in item.keys() else item['num']
#     edCd = '' if 'edCd' not in item.keys() else item['deCd']
#
#     jsonResult.append({'yyyymm':yyyymm,'natCd':natCd,'edCd':edCd,'num':num,'natKorNm':natKorNm})
#
#     return

def main():
    jsonResult = ''
    edCd = 'E'
    year = 2016
    month = 12
    jsonData = getTourPointVisitor(edCd)
    if(jsonData['response']['header']['resultMsg']=='OK'):
        jsonResult = jsonData['response']['body']['items']['item']

    jsonResult = sorted(jsonResult,key=lambda i: i['num'], reverse=True)

    for i in range(10):
        print(str(i+1)+'위. '+ jsonResult[i]['natKorNm'] + ' : '+str(jsonResult[i]['num']))


if __name__ =='__main__':
    main()