import requests
import time
import js_get_aiqiyi_e


def main():

    veid = "08019d59aaa6b9eceac0480b905485cf"
    tvid = "6941642434528900"
    cid = 'qc_105105_100485'
    # str_n = "q=ct:1&po=1&ul=&upd=0&ptid=01010031010000000000&b={}".format(tvid) + "&v=0&pv=&pr=0&cv=1.0.2&sv=6.27.1-mars&gt=1&pc=&ea=1&veid={}&pt=0&ps=0&n=0&y=0&w=0&ca=0&cd=0".format(veid)
    str_n = "q=ct:1&po=1&ul=&upd=0&ptid=01010031010000000000&b=6941642434528900&v=0&pv=&pr=0&cv=1.0.2&sv=6.27.1-mars&gt=1&pc=&ea=1&veid=08019d59aaa6b9eceac0480b905485cf&pt=0&ps=0&n=0&y=0&w=0&ca=53&cd=10"
    str_e = js_get_aiqiyi_e.get_e_str(str_n, cid)
    url = 'https://t7z.cupid.iqiyi.com/show2'
    # print(str_e)
    show2_s = js_get_aiqiyi_e.get_u_str(veid + str(int(time.time() * 1000)))
    params = {'e': str_e,
              'a': cid,
              'cb': '_jqjsp_show_mars',
              's': show2_s,
              }
    headers = {
            'Host': 't7z.cupid.iqiyi.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    }
    res = requests.get(url, headers=headers, params=params)
    print(res.url)



main()


'http://t7z.cupid.iqiyi.com/show2?e=AF48RQoEF0BaYgAWRVgFEwQTOwwAE0FEXDsMAAEECQVBUG4BAQUBAAVvAQAABAgTE15pCAQEBwQHawIEBQYADEFTeUcNBRdAQ2IXQEIJCBMSFWIAHgUfAhMsRw0GGgoCX1JyXFFHQhZSKwwBFkRbCFcGPgwBE0dVXDsMAAgECQwVVmZQUVQHUgw6UlVRVwgBSVM9CAAABQgAPFcWQEAFBVcTLAwAE18NBXlIDQASTwhBRTxQDQACFlY7DAEA&h=1618990678751&a=qc_105105_100485&u=1ed2ec90244e63b31d8d953ddfd3f3d0&p=&s=a7dc7e7c76becc1d2a160c8498bdfb20&cb=_jqjsp_show_mars&_1618990860059='
'http://t7z.cupid.iqiyi.com/show2?e=AF48RQoEF0BaYgAWRVgFEwQTOwwAE0FEXDsMAAEECQVBUG4BAQUBAAVvAQAABAgTE15pCAQEBwQHawIEBQYADEFTeUcNBRdAQ2IXQEIJCBMSFWIAHgUfAhMsRw0GGgoCX1JyXFFHQhZSKwwBFkRbCFcGPgwBE0dVXDsMAAgECQwVVmZQUVQHUgw6UlVRVwgBSVM9CAAABQgAPFcWQEAFBVcTLAwAE18NBXlIDQASTwhBRTxQDQACFlY7DAEA&a=qc_105105_100485&cb=_jqjsp_show_mars&s=12794f8aa93b4e942fb4c3a014d76622'