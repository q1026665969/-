# -*- coding: utf-8 -*-
import pprint
import time
import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import parsel

hot_country = ['北京', '上海', '广州', '深圳', '杭州', '天津', '西安',
               '苏州', '武汉', '厦门', '长沙', '成都', '郑州',
               '重庆', '宁波', '义乌', '福州', '泉州', '昆明']
dict_boss = {
    '鞍山': '101070300',
    '安康': '101110700',
    '安阳': '101180200',
    '安庆': '101220600',
    '安顺': '101260300',
    '澳门': '101330100',
    '阿拉善': '101081200',
    '阿里': '101140700',
    '阿克苏': '101131000',
    '阿勒泰': '101131500',
    '阿拉尔': '101131700',
    '北京': '101010100',
    '白城': '101060500',
    '白山': '101060800',
    '本溪': '101070500',
    '包头': '101080200',
    '巴彦淖尔': '101080800',
    '保定': '101090200',
    '宝鸡': '101110900',
    '滨州': '101121100',
    '白银': '101161000',
    '蚌埠': '101220200',
    '亳州': '101220900',
    '毕节': '101260500',
    '巴中': '101270900',
    '保山': '101290300',
    '百色': '101301000',
    '北海': '101301300',
    '巴音郭楞': '101130400',
    '博尔塔拉': '101130500',
    '白沙': '101311400',
    '保亭': '101311800',
    '北屯市': '101132100',
    '重庆': '101040100',
    '长春': '101060100',
    '朝阳': '101071200',
    '赤峰': '101080500',
    '承德': '101090400',
    '沧州': '101090700',
    '长治': '101100500',
    '常州': '101191100',
    '滁州': '101221000',
    '池州': '101221500',
    '长沙': '101250100',
    '郴州': '101250500',
    '常德': '101250600',
    '成都': '101270100',
    '潮州': '101281500',
    '崇左': '101300200',
    '楚雄': '101291700',
    '昌吉': '101130300',
    '澄迈': '101311200',
    '昌江黎族自治县': '101311500',
    '昌都': '101140300',
    '大庆': '101050800',
    '大连': '101070200',
    '丹东': '101070600',
    '大同': '101100200',
    '德州': '101120400',
    '东营': '101121200',
    '定西': '101160200',
    '达州': '101270600',
    '德阳': '101271700',
    '东莞': '101281600',
    '德宏': '101291300',
    '迪庆': '101291500',
    '大理': '101291600',
    '大兴安岭': '101051300',
    '儋州': '101310400',
    '东方': '101310900',
    '定安': '101311000',
    '东沙群岛': '101282200',
    '鄂尔多斯': '101080600',
    '鄂州': '101200300',
    '恩施': '101201300',
    '阿坝': '101271900',
    '抚顺': '101070400',
    '阜新': '101070900',
    '阜阳': '101220800',
    '福州': '101230100',
    '抚州': '101240400',
    '佛山': '101280800',
    '防城港': '101301400',
    '固原': '101170400',
    '赣州': '101240700',
    '贵阳': '101260100',
    '广安': '101270800',
    '广元': '101271800',
    '广州': '101280100',
    '桂林': '101300500',
    '贵港': '101300800',
    '甘孜': '101272100',
    '甘南': '101161400',
    '果洛': '101150600',
    '哈尔滨': '101050100',
    '黑河': '101050600',
    '鹤岗': '101051100',
    '葫芦岛': '101071400',
    '呼和浩特': '101080100',
    '呼伦贝尔': '101080700',
    '衡水': '101090800',
    '邯郸': '101091000',
    '汉中': '101110800',
    '菏泽': '101121000',
    '海东': '101150200',
    '鹤壁': '101181200',
    '淮安': '101190900',
    '黄冈': '101200500',
    '黄石': '101200600',
    '杭州': '101210100',
    '湖州': '101210200',
    '合肥': '101220100',
    '淮南': '101220400',
    '淮北': '101221100',
    '黄山': '101221600',
    '衡阳': '101250400',
    '怀化': '101251200',
    '惠州': '101280300',
    '河源': '101281200',
    '贺州': '101300700',
    '河池': '101301200',
    '海口': '101310100',
    '红河': '101291200',
    '海北': '101150300',
    '黄南': '101150400',
    '海南藏族自治州': '101150500',
    '海西': '101150800',
    '哈密': '101130900',
    '和田': '101131300',
    '佳木斯': '101050400',
    '鸡西': '101051000',
    '吉林': '101060200',
    '锦州': '101070700',
    '晋中': '101100400',
    '晋城': '101100600',
    '济南': '101120100',
    '济宁': '101120700',
    '金昌': '101160600',
    '酒泉': '101160800',
    '嘉峪关': '101161200',
    '焦作': '101181100',
    '荆州': '101200800',
    '荆门': '101201200',
    '嘉兴': '101210300',
    '金华': '101210900',
    '九江': '101240200',
    '吉安': '101240600',
    '景德镇': '101240800',
    '江门': '101281100',
    '揭阳': '101281900',
    '济源': '101181800',
    '克拉玛依': '101130200',
    '开封': '101180800',
    '昆明': '101290100',
    '克孜勒苏柯尔克孜自治州': '101131100',
    '喀什': '101131200',
    '可克达拉市': '101132200',
    '昆玉市': '101132300',
    '辽源': '101060600',
    '辽阳': '101071000',
    '廊坊': '101090600',
    '临汾': '101100700',
    '吕梁': '101101100',
    '临沂': '101120900',
    '聊城': '101121700',
    '拉萨': '101140100',
    '兰州': '101160100',
    '陇南': '101161100',
    '洛阳': '101180900',
    '漯河': '101181500',
    '连云港': '101191000',
    '丽水': '101210800',
    '六安': '101221400',
    '龙岩': '101230700',
    '娄底': '101250800',
    '六盘水': '101260600',
    '泸州': '101271000',
    '乐山': '101271400',
    '临沧': '101290800',
    '丽江': '101290900',
    '柳州': '101300300',
    '来宾': '101300400',
    '凉山': '101272000',
    '临夏': '101161300',
    '临高': '101311300',
    '乐东': '101311600',
    '陵水': '101311700',
    '林芝': '101140400',
    '牡丹江': '101050300',
    '马鞍山': '101220500',
    '绵阳': '101270400',
    '眉山': '101271500',
    '梅州': '101280400',
    '茂名': '101282000',
    '南阳': '101180700',
    '南京': '101190100',
    '南通': '101190500',
    '宁波': '101210400',
    '宁德': '101230300',
    '南平': '101230900',
    '南昌': '101240100',
    '南充': '101270500',
    '内江': '101271200',
    '南宁': '101300100',
    '怒江': '101291400',
    '那曲': '101140600',
    '盘锦': '101071300',
    '平凉': '101160300',
    '平顶山': '101180500',
    '濮阳': '101181300',
    '莆田': '101230400',
    '萍乡': '101240900',
    '攀枝花': '101270200',
    '普洱': '101290500',
    '齐齐哈尔': '101050200',
    '七台河': '101050900',
    '秦皇岛': '101091100',
    '青岛': '101120200',
    '庆阳': '101160400',
    '衢州': '101211000',
    '泉州': '101230500',
    '清远': '101281300',
    '曲靖': '101290200',
    '钦州': '101301100',
    '黔东南': '101260700',
    '黔南': '101260800',
    '黔西南': '101260900',
    '潜江': '101201500',
    '琼海': '101310600',
    '琼中': '101311900',
    '日照': '101121500',
    '日喀则': '101140200',
    '上海': '101020100',
    '绥化': '101050500',
    '双鸭山': '101051200',
    '四平': '101060300',
    '松原': '101060700',
    '沈阳': '101070100',
    '石家庄': '101090100',
    '朔州': '101100900',
    '商洛': '101110600',
    '石嘴山': '101170200',
    '商丘': '101181000',
    '三门峡': '101181700',
    '苏州': '101190400',
    '宿迁': '101191300',
    '十堰': '101201000',
    '随州': '101201100',
    '绍兴': '101210500',
    '宿州': '101220700',
    '三明': '101230800',
    '上饶': '101240300',
    '邵阳': '101250900',
    '遂宁': '101270700',
    '韶关': '101280200',
    '汕头': '101280500',
    '深圳': '101280600',
    '汕尾': '101282100',
    '三亚': '101310200',
    '三沙': '101310300',
    '神农架': '101201700',
    '山南': '101140500',
    '石河子': '101131600',
    '双河市': '101132400',
    '天津': '101030100',
    '通化': '101060400',
    '铁岭': '101071100',
    '通辽': '101080400',
    '唐山': '101090500',
    '太原': '101100100',
    '铜川': '101111000',
    '泰安': '101120800',
    '天水': '101160900',
    '泰州': '101191200',
    '台州': '101210600',
    '铜陵': '101221200',
    '铜仁': '101260400',
    '天门': '101201600',
    '屯昌': '101311100',
    '吐鲁番': '101130800',
    '塔城': '101131400',
    '图木舒克': '101131800',
    '铁门关': '101132000',
    '台湾': '101341100',
    '乌海': '101080300',
    '乌兰察布': '101080900',
    '渭南': '101110500',
    '潍坊': '101120600',
    '威海': '101121300',
    '乌鲁木齐': '101130100',
    '武威': '101160500',
    '吴忠': '101170300',
    '无锡': '101190200',
    '武汉': '101200100',
    '温州': '101210700',
    '芜湖': '101220300',
    '梧州': '101300600',
    '文山': '101291100',
    '五指山': '101310500',
    '文昌': '101310700',
    '万宁': '101310800',
    '五家渠': '101131900',
    '邢台': '101090900',
    '忻州': '101101000',
    '西安': '101110100',
    '咸阳': '101110200',
    '西宁': '101150100',
    '新乡': '101180300',
    '许昌': '101180400',
    '信阳': '101180600',
    '徐州': '101190800',
    '襄阳': '101200200',
    '孝感': '101200400',
    '咸宁': '101200700',
    '宣城': '101221300',
    '厦门': '101230200',
    '新余': '101241000',
    '湘潭': '101250200',
    '香港': '101320300',
    '湘西': '101251400',
    '西双版纳': '101291000',
    '仙桃': '101201400',
    '锡林郭勒': '101081000',
    '兴安盟': '101081100',
    '伊春': '101050700',
    '营口': '101070800',
    '阳泉': '101100300',
    '运城': '101100800',
    '延安': '101110300',
    '榆林': '101110400',
    '烟台': '101120500',
    '银川': '101170100',
    '扬州': '101190600',
    '盐城': '101190700',
    '宜昌': '101200900',
    '宜春': '101240500',
    '鹰潭': '101241100',
    '益阳': '101250700',
    '岳阳': '101251000',
    '永州': '101251300',
    '宜宾': '101271100',
    '雅安': '101271600',
    '云浮': '101281400',
    '阳江': '101281800',
    '玉溪': '101290400',
    '玉林': '101300900',
    '延边': '101060900',
    '玉树': '101150700',
    '伊犁': '101130600',
    '张家口': '101090300',
    '淄博': '101120300',
    '枣庄': '101121400',
    '张掖': '101160700',
    '中卫': '101170500',
    '郑州': '101180100',
    '周口': '101181400',
    '驻马店': '101181600',
    '镇江': '101190300',
    '舟山': '101211100',
    '漳州': '101230600',
    '株洲': '101250300',
    '张家界': '101251100',
    '遵义': '101260200',
    '自贡': '101270300',
    '资阳': '101271300',
    '珠海': '101280700',
    '肇庆': '101280900',
    '湛江': '101281000',
    '中山': '101281700',
    '昭通': '101290700'}


class Webdriver:
    def __init__(self):  # 进入目标页面完成条件选择
        self.proxyServer = "transfer.mogumiao.com:9001"
        self.proxyAuth = "Basic " + 'ZFFxMVUzUTZRNURDVnRKNzoxbWpDVVJiMjl0eXNIQlZv'
        path = 'D:\\编程\\上课文件\\爬虫进阶\\08 selenium\\08-00-正心-作业\\chromedriver.exe'
        options = webdriver.ChromeOptions()  # 保存浏览器设置
        # options.add_argument('--headless')  # 设置为无头浏览器
        options.add_argument('--no-sandbox')
        options.add_argument('window-size=1800x1200')  # 设置分辨率，改变分辨率可能会报错
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片
        options.add_argument('--disable-gpu')  # 谷歌文档指示用此规避bug
        options.add_argument('--proxy-server=socks5://{}'.format(self.proxyServer))
        self.driver = webdriver.Chrome(executable_path=path,  # './chromedriver',
                                       options=options)  # chromedriver加载路径


    def get_qv_ming(self, url):
        ls = []
        path = '.condition-district.show-condition-district  dd a'
        self.driver.get(url)
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, path))
        )
        aa = self.driver.find_elements_by_css_selector(path)
        for a in aa:
            if a.text == '不限':
                continue
            ls.append(a.text)
        return ls

    def set_proxy(self):
        pass

    def click_next_page(self):
        next_path = 'a.next'
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, next_path)))
        self.driver.find_element_by_css_selector(next_path).click()

    def yield_data(self, data):
        pass

    def get_info(self, html, city):
        # data = parsel.Selector(html)
        html = parsel.Selector(html)
        uls = html.css('.job-list ul li')
        d = {}
        d['city'] = city
        d['site'] = 'boss_直聘'
        for i in uls:
            job_name = i.css('.job-name a::text').get()
            d['job_name'] = job_name
            job_address = i.css('.job-area::text').get()
            d['job_address'] = job_address
            salary = i.css('.red::text').get()
            d['salary'] = salary
            req = i.css('.job-limit.clearfix p::text').get()
            d['req'] = req
            company_name = i.css('.company-text .name a::text').get()
            d['company_name'] = company_name
            company_str = i.css('.company-text p::text').getall()
            d['company_str'] = str(company_str)
            introduce = i.css('.info-desc::text').get()
            d['introduce'] = introduce
            pprint.pprint(d)
            self.yield_data(d)

    def start(self, url, city):
        self.driver.get(url)
        while True:
            time.sleep(1)
            html = self.driver.page_source
            if '当前IP地址可能存在异常访问行为，完成验证后即可正常使用' in html:
                print('----------error----------')
                break
            self.get_info(html, city)
            if self.driver.find_element_by_css_selector('a.next'):
                try:
                    self.click_next_page()
                except Exception as e:
                    if 'no such element' in e:
                        pass
                    else:
                        print(e)
                    break
            else:
                break

    def __del__(self):
        self.driver.quit()

    def close(self):
        self.driver.quit()


a = Webdriver()
for key in dict_boss.keys():
    try:
        if key in hot_country:
            url = 'https://www.zhipin.com/c{}/?query=跨境电商'.format(dict_boss[key])

            qv_ming = a.get_qv_ming(url)
            # 返回一个列表，热点城市的区名
            a.close()
            for s in qv_ming:
                url = 'https://www.zhipin.com/c{}/b_{}/?query=跨境电商'.format(dict_boss[key], s)

                a.start(url, key)
                a.close()
            continue
        else:
            url = 'https://www.zhipin.com/c{}/?query=跨境电商'.format(dict_boss[key])

            html = a.start(url, key)
            a.close()
            time.sleep(1)
    except Exception as e:
        a = Webdriver()
        print(e)
