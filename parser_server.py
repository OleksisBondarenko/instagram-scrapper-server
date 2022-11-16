from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

import time

import json

HTML_PATH = "index.html"

OUTPUT_PATH = "result.json"

ENCODING_FILE = "utf-8"

CHROME_DRIVER_PATH = r"D:\python_projects\get_info_from_instagram\chromedriver.exe"

TEST_URL = "https://instanavigation.com/ru/profile/zelenskiy_official"

MAX_RESPONSE_TIME = 10

IMPLICITLI_TIME = 0.5

def get_html_from_url(url=TEST_URL, chromedriver=CHROME_DRIVER_PATH):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-notifications')

    # with  webdriver.Chrome(chromedriver, chrome_options=chrome_options) as driver:
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    driver.implicitly_wait(IMPLICITLI_TIME)
    try: 
        driver.get(url)
    except: 
        raise Exception("Lost internet connection")
    # wait = WebDriverWait(driver, MAX_RESPONSE_TIME)
    # wait.until()
    PAUSE_TIME = 3
    try:
        driver.execute_script(
            "document.getElementsByClassName('profile-publications__btn')[0].click();")
        time.sleep(PAUSE_TIME)
    except Exception:
        driver.close()
    
    try:
        Alert(driver).accept()
    except:
        print("no alert")
    page_source = driver.page_source
    driver.close()
    return page_source

def get_info_about_user_by_url(url):
    html_content = get_html_from_url(url)
    # html_content = read_data_from_file()
    soup = BeautifulSoup(html_content, "lxml")

    def get_nickname ():
        return soup.find('p', class_="profile-login").getText()


    def get_three_last_posts ():
        raw_posts = soup.find("div", id="posts").find_all(
            "div", class_="col-lg-4 col-md-4 col-12 post-wrapper")

        map_posts = map(lambda post: {
            "image": post.find("img", class_="publications__img")['src'],
            "date": post.find("p", class_="text-dark mb-1 mt-3").text,
            "description": post.find("p", class_="text-dark mt-1").text
        }, raw_posts)

        return list(map_posts)[:3]


    def get_main_image ():
        return soup.find("img", class_="profile-photo__png")["src"]  


    def get_main_info (): 
        main_info_block = soup.find("div", class_="d-md-flex d-none mt-3").find_all("p", class_="profile__info-title")
        publications_count = main_info_block[0].text
        subscribers_count = main_info_block[1].text
        subscribed_count = main_info_block[2].text
        
        return {"publications_count": publications_count, "subscribed_count": subscribed_count, "subscribers_count": subscribers_count}


    def get_biography (): 
        return soup.find("p", class_="biography").text


    def get_profile_name ():
        return soup.find("p", class_="profile__name d-md-block").text
    

    nickname = get_nickname()
    posts = get_three_last_posts()
    main_image = get_main_image()
    main_info = get_main_info()
    profile_name = get_biography()
    biography = get_profile_name()
    
    userInfo = {"nickname": nickname, "main_image": main_image, "main_info": main_info, "profile_name": profile_name, "biography": biography, "posts": posts}
    # json_version = json.dumps(userInfo, ensure_ascii=False)

    return userInfo


def app (): 
    user_info = get_info_about_user_by_url(TEST_URL)
    print(user_info)

if __name__ == '__main__':
    app()
