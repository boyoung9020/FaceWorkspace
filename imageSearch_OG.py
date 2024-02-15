import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests



def scroll_to_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def remove_invalid_images(images_dir):
    print("-" * 40, "이미지 필터링 중", "-" * 40)
    deleted_count = 0
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):
            file_path = os.path.join(images_dir, filename)
            if os.path.getsize(file_path) == 122:
                print(f"정상적이지 않은 이미지: {filename}, 삭제됨")
                os.remove(file_path)
                deleted_count += 1
    print('-' * 102)
    print(f"삭제된 이미지 수: {deleted_count}")

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
    time.sleep(1)

    num_scrolls =num_images // 20  # 한 번의 스크롤마다 대략 20개의 이미지가 로드됨
    starttime = time.time()
    print("image loading..   (maximum 25s)")
    for _ in range(num_scrolls):
        scroll_to_end(driver)
        try:
            more_results_button = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')
            more_results_button.click()
            time.sleep(1)

        except Exception as e:
            print("image load complete")
            break
    endtime = time.time()
    elapsed_time = endtime - starttime
    elapsed_time_seconds = int(elapsed_time)
    print("total load time :", elapsed_time_seconds, "s")
    print('-' * 102)
    image_elements = driver.find_elements(By.XPATH, '//*[@id="islrg"]//img[contains(@class,"rg_i")]')
    saved_images_count = 1

    starttime = time.time()

    for i, image_element in enumerate(image_elements):
        if saved_images_count >= num_images:
            break
        try:
            image_element.click()
            time.sleep(1)
            detailed_image = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img')
            image_url = detailed_image.get_attribute('src')
            image_name = f"{search_term}_{saved_images_count}.jpg"
            image_path = os.path.join(images_dir, image_name)
            with open(image_path, 'wb') as f:
                f.write(requests.get(image_url).content)
            print(f"save : {image_name}")
            saved_images_count += 1
        except Exception as e:
            pass

    print(f"다운로드된 이미지 수: {saved_images_count}")
    driver.quit()


    endtime = time.time()
    elapsed_time = endtime - starttime
    elapsed_time_seconds = int(elapsed_time)
    print("total save time : ", elapsed_time_seconds, "s")

    remove_invalid_images(images_dir)


def main():
    search_term = input("검색어를 입력하세요: ")
    num_images = int(input("다운로드할 이미지의 수를 입력하세요: "))
    save_images(search_term, num_images)

if __name__ == "__main__":
    main()
