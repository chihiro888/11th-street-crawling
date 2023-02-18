import time
from selenium import webdriver


def get_category(keyword):
    # custom parameter
    url = f'https://search.11st.co.kr/Search.tmall?kwd={keyword}'
    delay_sec = 3

    # crawling
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element("xpath", '//*[@id="layBodyWrap"]/div/div/div[3]/div/section[1]/ul/li[1]/div').click()
    time.sleep(delay_sec)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(delay_sec)
    el = driver.find_element('xpath', '//*[@id="layBodyWrap"]/div/div[1]/div[2]/div/div[1]/div[1]/ol/li[4]/div/div[1]/em')
    result = el.text
    time.sleep(delay_sec)
    driver.quit()

    return result

    
def main():
    # INPUT
    keyword = '포켓몬'

    # OUTPUT
    result = get_category(keyword)
    print(result)
    

if __name__ == "__main__":
    main()