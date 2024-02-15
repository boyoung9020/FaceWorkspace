import requests
import os

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create directory if it doesn't exist
        with open(save_path, 'wb') as file:
            file.write(response.content)


def search_and_download_images(search_term, api_key, cse_id, num_images):
    search_url = f"https://www.googleapis.com/customsearch/v1?q={search_term}&cx={cse_id}&key={api_key}&searchType=image&num={num_images}"
    response = requests.get(search_url)
    search_results = response.json()

    for idx, item in enumerate(search_results.get('items', []), start=1):
        image_url = item['link']
        save_path = os.path.join('downloaded_images', f"{search_term}_{idx}.jpg")
        download_image(image_url, save_path)
        print(f"Downloaded {save_path}")


def main():
    api_key = 'AIzaSyC9Va0fbqU86JvEOF2-ILwXdwPAf_DTtag'
    cse_id = 'f3a2ae7ae0c6341f4'
    search_term = input("검색어를 입력하세요: ")
    num_images = int(input("다운로드할 이미지의 수를 입력하세요: "))
    search_and_download_images(search_term, api_key, cse_id,  num_images)

if __name__ == "__main__":
    main()
