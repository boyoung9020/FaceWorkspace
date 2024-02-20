import requests
import os
import time
import face_check
from tqdm import tqdm

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  

        with open(save_path, 'wb') as file:
            file.write(response.content)

def remove_invalid_images(images_dir,name):
    print("\n" + "-" * 40, "이미지 필터링 중", "-" * 40)
    print("1단계 필터링..")
    deleted_count = 0
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):
            txt_path = os.path.join(images_dir, filename)
            if os.path.getsize(txt_path) < 10240:
                print(f"정상적이지 않은 이미지: {filename}, 삭제됨")
                os.remove(txt_path)
                deleted_count += 1
    print("\n2단계 필터링..") 
    print("\nloaded face_cehck.py\n")
    deleted_count += face_check.main(name)  
    print(f"삭제된 이미지 수: {deleted_count}")

    print('-' * 98)



def search_and_download_images(person_name, api_key, cse_id, num_images):
    print("\n" + "-" * 43 + f" {person_name} " + "-" * 43)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'Person_archive', person_name)
    os.makedirs(images_dir, exist_ok=True)
    
    starttime = time.time()
    search_url = f"https://www.googleapis.com/customsearch/v1?q={person_name}&cx={cse_id}&key={api_key}&searchType=image&num={num_images}"
    response = requests.get(search_url)
    search_results = response.json()
    saved_images_count = 0
    
    with tqdm(total=num_images,desc=person_name,unit='image') as pbar:
        for idx, item in enumerate(search_results.get('items', []), start=1):
            if saved_images_count == num_images:
                break
            
            image_url = item['link']
            image_name = f"{person_name}_{idx}.jpg"
            save_path = os.path.join(images_dir, image_name)
            download_image(image_url, save_path)
            # print(f"Downloaded : {save_path}")
            # print(f"저장 완료: {image_name}")
            saved_images_count += 1
            pbar.update(1)

    print()           
    print(f"다운로드된 이미지 수: {saved_images_count}")
    endtime = time.time()
    elapsed_time = endtime - starttime
    elapsed_time_seconds = int(elapsed_time)
    print("총 저장 시간:", elapsed_time_seconds, "초")
    remove_invalid_images(images_dir, person_name)

def main(num_images):
    api_key = 'AIzaSyC9Va0fbqU86JvEOF2-ILwXdwPAf_DTtag'
    cse_id = 'f3a2ae7ae0c6341f4'
    # search_term = input("검색어를 입력하세요: ")
    # num_images = int(input("다운로드할 이미지의 수를 입력하세요: "))
    # search_and_download_images(search_term, api_key, cse_id,  num_images)
    num_images = num_images
    txt_path = "./인물리스트.txt"
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            person_list = file.readlines()
            for person in person_list:
                person_name = person.strip()  
                search_and_download_images(person_name, api_key, cse_id,  num_images)
    except FileNotFoundError:
        print(f"Error: 파일 '{txt_path}'을 찾을 수 없습니다.")
    except Exception as e:
        print(f"Error: {e}")





# if __name__ == "__main__":
#     main()
