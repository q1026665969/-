import asyncio
import parsel
import time
from pyppeteer import launch


# 拿到数据，保存数据
def get_info(html):
    selector = parsel.Selector(html)
    tbody = selector.css('tbody')
    tr1 = tbody[3].css('tr')
    print(len(tr1))
    tr = list(tr1)
    tr.remove(tr[0])
    for i in tr:
        td1 = i.css('td')
        td = list(td1)
        td = td[6:]
        for name in td:
            t_ = name.css('::attr(title)').get()
            if t_:
                pass
            else:
                t_ = 'none'
            # f.write(t_+',')
            print(t_, end='  ')
        print()
        # f.write('\n')


async def main():
    # 运行浏览器
    exe_path = 'D:\\编程\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.goto('https://www3.wipo.int/branddb/en/#', options={"timeout": 50000})
    await asyncio.sleep(1)
    # 调整显示一百条数据
    page_100 = '#results > div.results_navigation.top_results_navigation.displayButtons > div.results_pager.ui-widget-content > div.rowCountContainer.lightBackground > span > div.rowCountSelectContainer > ul > li > ul > li:nth-child(4) > a'
    xianshi = await page.querySelector('#results > div.results_navigation.top_results_navigation.displayButtons > div.results_pager.ui-widget-content > div.rowCountContainer.lightBackground > span > div.rowCountSelectContainer > ul > li')
    await xianshi.hover()
    time.sleep(3)
    await page.waitFor(2000)
    await page.waitFor(page_100)  # 等待选项出现
    await page.click(page_100)
    time.sleep(8)
    input_page = '#skipValue1'
    await page.type(input_page, '50')
    await page.keyboard.press('Enter')
    time.sleep(15)
    # 循环点击下一页
    page = 1
    while True:
        try:
            time.sleep(3)
            page_text = await page.content()
            get_info(page_text)
            next_path = '#results > div.results_navigation.top_results_navigation.displayButtons > div.results_pager.ui-widget-content > div.arrow_container > a:nth-child(4) > span.ui-button-icon-primary.ui-icon.ui-icon-triangle-1-e'
            next_ = await page.querySelector(next_path)
            await next_.click()
            time.sleep(2)
            page += 1
        except:
            pass
        if 1:
            break
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
