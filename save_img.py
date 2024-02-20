import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import googleCSE
import subprocess
import face_check
from tqdm import tqdm

def scroll_to_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def remove_invalid_images(images_dir,name):
    print("\n" + "-" * 40, "이미지 필터링 중", "-" * 40)
    print("1단계 필터링..")

    deleted_count = 0
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):
            file_path = os.path.join(images_dir, filename)
            if os.path.getsize(file_path) < 10240:
                print(f"정상적이지 않은 이미지: {filename}, 삭제됨")
                os.remove(file_path)
                deleted_count += 1
    print("\n2단계 필터링..")   
    print("\nloaded face_cehck.py\n")
    deleted_count += face_check.main(name)  
    print(f"삭제된 이미지 수: {deleted_count}")

    print('-' * 98)



def save_images_for_person(person_name, num_images):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'Person_archive', person_name)
    os.makedirs(images_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.google.com/search?tbm=isch&q={person_name}"
    driver.get(search_url)
    time.sleep(1)

    num_scrolls = (num_images // 20) +1  

    starttime = time.time()
    print("이미지 로딩 중... (최대 25초)")
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
    print("총 로드 시간:", elapsed_time_seconds, "초")
    print("\n" + "-" * 43 + f" {person_name} " + "-" * 43)
    image_elements = driver.find_elements(By.XPATH, '//*[@id="islrg"]//img[contains(@class,"rg_i")]')
    saved_images_count = 1

    starttime = time.time()

    with tqdm(total=num_images,desc=person_name,unit='image') as pbar:
        for i, image_element in enumerate(image_elements):
            try:
                if saved_images_count - 1 == num_images:
                    break
                image_element.click()
                time.sleep(1)
                detailed_image = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img')
                image_url = detailed_image.get_attribute('src')
                image_name = f"{person_name}_{saved_images_count}.jpg"
                image_path = os.path.join(images_dir, image_name)
                with open(image_path, 'wb') as f:
                    f.write(requests.get(image_url).content)
                # print(f"저장 완료: {image_name}")
                saved_images_count += 1
                pbar.update(1)
            except Exception as e:
                pass
    print()           
    print(f"다운로드된 이미지 수: {saved_images_count - 1}")
    driver.quit()

    endtime = time.time()
    elapsed_time = endtime - starttime
    elapsed_time_seconds = int(elapsed_time)
    print("총 저장 시간:", elapsed_time_seconds, "초")

    remove_invalid_images(images_dir,person_name)

def selenium(num_images):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            person_list = file.readlines()
            for person in person_list:
                search_term = person.strip()
                save_images_for_person(search_term,num_images)
    except FileNotFoundError:
        print(f"Error: 파일 '{file_path}'을 찾을 수 없습니다.")
    except Exception as e:
        print(f"Error: {e}")

def open_notepad(file_path):
    try:
        return subprocess.Popen(["notepad.exe", file_path])
    except Exception as e:
        print(f"Error occurred while opening Notepad: {e}")
        return None

file_path = "./인물리스트.txt"

if __name__ == "__main__":
    print("다운로드 할 이름을 메모장에 한줄씩 적고 닫아주세요.")

    process = open_notepad(file_path)
    
    process.communicate()


    num_images = int(input("인물 별 저장할 이미지 갯수 : "))    
    if(num_images > 10) :
        print("\n*** Select selenium")
        selenium(num_images)
    else :    
        print("\n*** Select googleCSE")
        googleCSE.main(num_images)
