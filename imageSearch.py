import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import base64

def scroll_to_end(driver):
    # 현재 페이지의 스크롤 위치 저장
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 스크롤을 맨 아래로 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # 새로운 스크롤 위치 가져오기
        new_height = driver.execute_script("return document.body.scrollHeight")
        # 스크롤이 변하지 않으면 스크롤 중지
        if new_height == last_height:
            break
        # 다음 스크롤을 위해 현재 스크롤 위치 업데이트
        last_height = new_height

def save_images(search_term, num_images):
    script_dir = os.path.dirname(__file__)
    images_dir = os.path.join(script_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    options = webdriver.ChromeOptions()

    options.add_argument('--headless')  
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.google.com/search?tbm=isch&q={search_term}"
    driver.get(search_url)
    time.sleep(2) 


    num_scrolls =num_images // 20  # 한 번의 스크롤마다 대략 20개의 이미지가 로드됨
    starttime = time.time()
    print("이미지 로드중(최대 25초)")
    for _ in range(num_scrolls):
        scroll_to_end(driver)
        try:
            more_results_button = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')
            more_results_button.click()
            time.sleep(1) 
        except Exception as e:
            print("이미지 로드 완료")
            break
    endtime = time.time()
    elapsed_time = endtime - starttime
    elapsed_time_seconds = int(elapsed_time)
    print("경과 시간:", elapsed_time_seconds, "초")

    img_tags = driver.find_elements(By.XPATH, '//img[contains(@class,"rg_i")]')
    img_urls = [img_tag.get_attribute('src') for img_tag in img_tags]

    downloaded_images = 0
    for idx, img_data_base64 in enumerate(img_urls[:20]):
        try:
            # base64로 인코딩된 이미지 데이터를 디코드하여 바이너리 데이터로 변환
            img_data = base64.b64decode(img_data_base64.split(',')[1])

            with open(os.path.join(images_dir, f'{search_term}_{downloaded_images + 1}.jpg'), 'wb') as handler:
                handler.write(img_data)

            print(f"다운로드 완료: {search_term}_{downloaded_images + 1}.jpg")
            downloaded_images += 1
        except Exception as e:
            pass

    for idx, img_url in enumerate(img_urls[20:]):
        try:
            if downloaded_images >= num_images:
                break

            img_data = requests.get(img_url).content
            with open(os.path.join(images_dir, f'{search_term}_{downloaded_images + 1}.jpg'), 'wb') as handler:
                handler.write(img_data)
            print(f"다운로드 완료: {search_term}_{downloaded_images + 1}.jpg")
            downloaded_images += 1
        except Exception as e:
            pass

    driver.quit()

def main():
    search_term = input("검색어를 입력하세요: ")
    num_images = int(input("다운로드할 이미지의 수를 입력하세요: "))
    save_images(search_term, num_images)

if __name__ == "__main__":
    main()
