import requests
import random
import time
import execjs
import re


ua = 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/90.0.4430.72 safari/537.36'
tvid = '10840052500'
url = ''


def export(in_e):
    export_ctx = execjs.compile("""
    function a(e, t) {
    e[t >> 5] |= 128 << t % 32,
    e[14 + (t + 64 >>> 9 << 4)] = t;
    for (var i = 1732584193, a = -271733879, n = -1732584194, l = 271733878, c = 0; c < e.length; c += 16) {
        var f = i
          , _ = a
          , h = n
          , p = l;
        i = r(i, a, n, l, e[c + 0], 7, -680876936),
        l = r(l, i, a, n, e[c + 1], 12, -389564586),
        n = r(n, l, i, a, e[c + 2], 17, 606105819),
        a = r(a, n, l, i, e[c + 3], 22, -1044525330),
        i = r(i, a, n, l, e[c + 4], 7, -176418897),
        l = r(l, i, a, n, e[c + 5], 12, 1200080426),
        n = r(n, l, i, a, e[c + 6], 17, -1473231341),
        a = r(a, n, l, i, e[c + 7], 22, -45705983),
        i = r(i, a, n, l, e[c + 8], 7, 1770035416),
        l = r(l, i, a, n, e[c + 9], 12, -1958414417),
        n = r(n, l, i, a, e[c + 10], 17, -42063),
        a = r(a, n, l, i, e[c + 11], 22, -1990404162),
        i = r(i, a, n, l, e[c + 12], 7, 1804603682),
        l = r(l, i, a, n, e[c + 13], 12, -40341101),
        n = r(n, l, i, a, e[c + 14], 17, -1502002290),
        a = r(a, n, l, i, e[c + 15], 22, 1236535329),
        i = o(i, a, n, l, e[c + 1], 5, -165796510),
        l = o(l, i, a, n, e[c + 6], 9, -1069501632),
        n = o(n, l, i, a, e[c + 11], 14, 643717713),
        a = o(a, n, l, i, e[c + 0], 20, -373897302),
        i = o(i, a, n, l, e[c + 5], 5, -701558691),
        l = o(l, i, a, n, e[c + 10], 9, 38016083),
        n = o(n, l, i, a, e[c + 15], 14, -660478335),
        a = o(a, n, l, i, e[c + 4], 20, -405537848),
        i = o(i, a, n, l, e[c + 9], 5, 568446438),
        l = o(l, i, a, n, e[c + 14], 9, -1019803690),
        n = o(n, l, i, a, e[c + 3], 14, -187363961),
        a = o(a, n, l, i, e[c + 8], 20, 1163531501),
        i = o(i, a, n, l, e[c + 13], 5, -1444681467),
        l = o(l, i, a, n, e[c + 2], 9, -51403784),
        n = o(n, l, i, a, e[c + 7], 14, 1735328473),
        a = o(a, n, l, i, e[c + 12], 20, -1926607734),
        i = s(i, a, n, l, e[c + 5], 4, -378558),
        l = s(l, i, a, n, e[c + 8], 11, -2022574463),
        n = s(n, l, i, a, e[c + 11], 16, 1839030562),
        a = s(a, n, l, i, e[c + 14], 23, -35309556),
        i = s(i, a, n, l, e[c + 1], 4, -1530992060),
        l = s(l, i, a, n, e[c + 4], 11, 1272893353),
        n = s(n, l, i, a, e[c + 7], 16, -155497632),
        a = s(a, n, l, i, e[c + 10], 23, -1094730640),
        i = s(i, a, n, l, e[c + 13], 4, 681279174),
        l = s(l, i, a, n, e[c + 0], 11, -358537222),
        n = s(n, l, i, a, e[c + 3], 16, -722521979),
        a = s(a, n, l, i, e[c + 6], 23, 76029189),
        i = s(i, a, n, l, e[c + 9], 4, -640364487),
        l = s(l, i, a, n, e[c + 12], 11, -421815835),
        n = s(n, l, i, a, e[c + 15], 16, 530742520),
        a = s(a, n, l, i, e[c + 2], 23, -995338651),
        i = d(i, a, n, l, e[c + 0], 6, -198630844),
        l = d(l, i, a, n, e[c + 7], 10, 1126891415),
        n = d(n, l, i, a, e[c + 14], 15, -1416354905),
        a = d(a, n, l, i, e[c + 5], 21, -57434055),
        i = d(i, a, n, l, e[c + 12], 6, 1700485571),
        l = d(l, i, a, n, e[c + 3], 10, -1894986606),
        n = d(n, l, i, a, e[c + 10], 15, -1051523),
        a = d(a, n, l, i, e[c + 1], 21, -2054922799),
        i = d(i, a, n, l, e[c + 8], 6, 1873313359),
        l = d(l, i, a, n, e[c + 15], 10, -30611744),
        n = d(n, l, i, a, e[c + 6], 15, -1560198380),
        a = d(a, n, l, i, e[c + 13], 21, 1309151649),
        i = d(i, a, n, l, e[c + 4], 6, -145523070),
        l = d(l, i, a, n, e[c + 11], 10, -1120210379),
        n = d(n, l, i, a, e[c + 2], 15, 718787259),
        a = d(a, n, l, i, e[c + 9], 21, -343485551),
        i = u(i, f),
        a = u(a, _),
        n = u(n, h),
        l = u(l, p)
    }
    return Array(i, a, n, l)
}
function n(e, t, i, a, n, r) {
    return u(l(u(u(t, e), u(a, r)), n), i)
}
function r(e, t, i, a, r, o, s) {
    return n(t & i | ~t & a, e, t, r, o, s)
}
function o(e, t, i, a, r, o, s) {
    return n(t & a | i & ~a, e, t, r, o, s)
}
function s(e, t, i, a, r, o, s) {
    return n(t ^ i ^ a, e, t, r, o, s)
}
function d(e, t, i, a, r, o, s) {
    return n(i ^ (t | ~a), e, t, r, o, s)
}
function u(e, t) {
    var i = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (i >> 16) << 16 | 65535 & i
}
function l(e, t) {
    return e << t | e >>> 32 - t
}
function c(e) {
    for (var t = Array(), i = (1 << h) - 1, a = 0; a < e.length * h; a += h)
        t[a >> 5] |= (e.charCodeAt(a / h) & i) << a % 32;
    return t
}
function f(e) {
    for (var t = _ ? "0123456789ABCDEF" : "0123456789abcdef", i = "", a = 0; a < 4 * e.length; a++)
        i += t.charAt(e[a >> 2] >> a % 4 * 8 + 4 & 15) + t.charAt(e[a >> 2] >> a % 4 * 8 & 15);
    return i
}
var _ = 0
  , h = 8;
exports = function(e) {
    return f(a(c(e), e.length * h))
}

    """)
    str_e = export_ctx.call('exports', in_e)
    return str_e


def get_ua(u, r_s, t):
    """
    o参数为记录用户进入次数
    :param u: 用户ua信息
    :return: 加密u参数
    """
    o = 20
    # u_str = u+str(random.random())+str(int(time.time()*1000)*o)
    u_str = u+str(r_s)+str(t*o)
    u_str = export(u_str)
    return u_str


def main_run(url_start, ua):
    url = url_start
    headers = {
    'user-agent': ua,
    }
    # veid,随机生成
    res1 = requests.get(url_start, headers=headers)
    print(res1.url)
    tvid = re.findall('param\[\'tvid\'\] = \"(.*?)\";', res1.text)[0]
    # dfp = 'a0794e8fffa25e4c21adeaac104bf5db57db69d426a660166e40a9659914766f03@1620112451626@1618816452626'
    dfp = 'a0794e8fffa25e4c21adeaac104bf5db57db69d426a660166e40a9659914766f03'
    # dfp = 'a0b72eb027e4f54e2b8eac346441272eacb4409b34214ac798e95f67fd8e6db7dd'
    print('dfp:', dfp)
    t_use1 = int(time.time()*1000)
    t_use = int(t_use1/1000)
    r_s = str(random.random())
    b_params = {
        # 使用exports()加密
        'u': get_ua(ua, r_s, t_use1),
        'pu': '',
        # 'rn': '0.23133886479095778',
        'rn': r_s,
        'p1': '1_10_101',
        'v': '1.0.2',
        # 记录参数
        'dfp': dfp,
        # sid  "weid"+new date  然后使用exports()加密 毫秒时间戳
        'ce': export("weid"+str(t_use1)),
        # 'ce': export("weid"+str(int(time.time()*1000))),
        # 取当前时间戳，s为单位
        'de': f'{t_use},{t_use},{t_use},1',
        'stime': t_use1,
        'c1': '8',
        # tvid 与下面fatherid一致
        'r': tvid,
        # "veid"+new date  然后使用exports()加密  毫秒时间戳
        # 've': export("veid"+str(int(time.time()*1000))),
        've': export("veid"+str(t_use1)),
        'ht': '0',
        'pt': '',
        'hu': '-1',
        'isdm': '0',
        'duby': '0',
        'ra': '2',
        'clt': '',
        's3': '',
        'ps2': '',
        'ps3': '',
        'ps4': '',
        'stype': '',
        'br': ua,
        'mod': 'cn_s',
        # 当前页面地址
        'purl': url,
        'tmplt': '',
        # 设备编号
        'ptid': '01010031010000000001',
        'os': 'window',
        # nu = s.getIsNewUser() ? 1 : 0
        'nu': '1',
        'vfm': '',
        'coop': '',
        # ispre = n.isTryWatch() ? 1 : 0,
        'ispre': '0',
        # 视频是否是3d
        'videotp': '0',
        'drm': '',
        'plyrv': '',
        # 视频来源 window.document.referrer
        # 'rfr': 'http://localhost:63342/',
        'rfr': 'https://so.iqiyi.com/',
        # 来源id h.albumId，地址tvid
        'fatherid': tvid,
        'stauto': '0',
        'algot': '',
        'ldt': '0',
        'vvfrom': '',
        's4': '',
        'pagev': '',
        'mft': '2',
        'wint': '3',
        's2': '',
        'engt': '2',
        'bw': '18',
        'ntwk': '18',
        'dl': '59.8',
        't': '15',
        '_': t_use1+random.randint(1, 10),
}
    time.sleep(0.5)
    res = requests.get('https://msg.qy.net/b', params=b_params, headers=headers)
    print(res.url)
    print(res.status_code)


if __name__ == '__main__':
    import os

    url_ls = ['http://www.iqiyi.com/v_19rwjce1lw.html', 'http://www.iqiyi.com/v_19rwi77vw0.html',
              'http://www.iqiyi.com/v_19rwm3sss0.html', 'http://www.iqiyi.com/v_19rwlkaro4.html',
              'http://www.iqiyi.com/v_19rwl0ecw4.html', 'http://www.iqiyi.com/v_19rwfgg8bw.html',
              'http://www.iqiyi.com/v_19rwhhwc6k.html', 'http://www.iqiyi.com/v_19rwho5854.html',
              'http://www.iqiyi.com/v_19rwhnsht4.html', 'http://www.iqiyi.com/v_19rwh0bhck.html']
    for i in url_ls:
        # os.system('ifdown ppp0')
        # os.system("ifup ppp0")
        main_run(i, ua)
        print('now: ', i)
