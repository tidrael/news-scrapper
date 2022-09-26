import json
from datetime import datetime as dt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def get_data():
    today = dt.now().strftime("%Y-%m-%d")

    driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()), chrome_options=chrome_options)
    url = "https://thoibaotaichinhvietnam.vn/"
    driver.get(url)

    head_list = driver.find_elements(
        By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div/div/article/div/h3/a")
    head_list = [item.text for item in head_list]

    media_list = driver.find_elements(
        By.XPATH, "/html/body/div/main/div[3]/div[2]/div[2]/div[2]/article/div/h3/a")
    media_list = [item.text for item in media_list]

    podcast_list = driver.find_elements(
        By.XPATH, "/html/body/div/main/div[3]/div[3]/div[2]/article/div/h3/a")
    podcast_list = [item.text for item in podcast_list]

    article_list = driver.find_elements(
        By.XPATH, "/html/body/div/main/div[6]/div[1]/div/div/article/div/h3/a")
    article_list = [item.text for item in article_list]

    url = "https://thoibaotaichinhvietnam.vn/doi-thoai"
    driver.get(url)
    talk_list = driver.find_elements(
        By.XPATH, "/html/body/div[1]/main/div[3]/div[1]/div[1]/div/article/div[2]/h3/a")
    talk_list = [item.text for item in talk_list]

    driver.close()
    driver.quit()

    inform_list = []
    list_dict = {
        "head": head_list,
        "media": media_list,
        "podcast": podcast_list,
        "article": article_list,
        "talk": talk_list,
    }
    for key, item in list_dict.items():
        for content in item:
            a_dict = {}
            a_dict["type"] = key
            a_dict["content"] = content
            inform_list.append(a_dict)

    data = {"day": today, "inform": inform_list}
    data_json = json.dumps(data, ensure_ascii=False)
    return data_json
