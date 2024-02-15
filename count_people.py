import dlib

def count_people(image_path):
    # 이미지 불러오기
    image = dlib.load_rgb_image(image_path)
    
    # 얼굴 검출기 초기화
    detector = dlib.get_frontal_face_detector()
    
    # 이미지에서 얼굴 검출
    dets = detector(image, 1)
    
    # 감지된 얼굴 수 반환
    return len(dets)

if __name__ == "__main__":
    image_path = r"D:\Workspace\images\example_image.jpg"  # 분석할 이미지 경로
    num_people = count_people(image_path)
    print("이미지 속 사람 수:", num_people)
