from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Chrome이 최신 버전이어야 함
# ChromeDriverManager: Chrome 은 업데이트가 자주 일어난다. 이를 해당 파이썬 프로그램에서 일일히 업데이트를 우리가 해주지 않아도 자동으로 해줌
def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://comic.naver.com/webtoon?tab=mon")
    sleep(1) # sleep(n) >> n초동안 켜졌다가 꺼짐

    # find_element & find_elements = querySelector & querySelectors
    days = driver.find_elements(by=By.CSS_SELECTOR, value="#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li")
    for day in days[1:3]: # slice, 배열의 1번 인덱스부터 8번 인덱스 전까지(즉, 7번 인덱스까지) 자를 수 있다
        # print(day.text)
        link = day.find_element(by=By.CSS_SELECTOR, value="a")
        # a테그에 해당되는 link 의 위치로 scroll을 통해 이동해라!
        driver.execute_script("arguments[0].scrollIntoView(true);", link) # 화면에 보이지 않으면 클릭을 할 수 없기 때문에 넣는 문장! click 등 scroll은 항상 있어야함!
        driver.execute_script("arguments[0].click()", link)
        sleep(1)

        webtoonDict = {}

        # 각 웹툰을 담기 위한 list 생성
        weekdayWebtoonList = []

        # 웹툰 하나하나 반복
        # 각 요일마다 해당 ul의 selector가 같은지 확인해야함!
        items = driver.find_elements(by=By.CSS_SELECTOR, value="#content > div:nth-child(1) > ul > li")
        for item in items:
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            imgElement = item.find_element(by=By.CSS_SELECTOR, value="a > div > img")
            imgSrc = imgElement.get_attribute("src")
            titleElement = item.find_element(by=By.CSS_SELECTOR, value="div > a > span > span")
            titleText = titleElement.text
            authorElement = item.find_element(by=By.CSS_SELECTOR, value="div > .ContentAuthor__author--CTAAP")
            authorText = authorElement.text
            ratingElement = item.find_element(by=By.CSS_SELECTOR, value="div > *:nth-child(3) > span > span")
            ratingText = ratingElement.text
            weekdayWebtoonList.append({
                "표지": imgSrc,
                "제목": titleText,
                "저자": authorText,
                "평점": ratingText
            })
            sleep(0.2)
        webtoonDict[day.text] = weekdayWebtoonList
    print(webtoonDict)