from PIL import Image, ImageDraw
import face_recognition
import os
# 입력 및 출력 디렉토리 경로 설정
input_dir = "D:/FaceWorkspace/images/"  # 이미지 폴더의 새 경로로 수정
output_dir = "D:/FaceWorkspace/images2/"  # 결과 이미지를 저장할 새 폴더

# 입력 디렉토리의 모든 파일 목록 가져오기
image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# 모든 이미지에 대해 처리
for image_file in image_files:
    # 이미지 파일의 상대 경로 생성
    image_path = os.path.join(input_dir, image_file)

    # 이미지 파일을 numpy 배열로 로드
    image = face_recognition.load_image_file(image_path)

    # 이미지에서 모든 얼굴의 특징 찾기
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("Found {} face(s) in {}".format(len(face_landmarks_list), image_file))

    # PIL ImageDraw 객체 생성
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    # 얼굴 특징 그리기
    for face_landmarks in face_landmarks_list:
        for facial_feature in face_landmarks.keys():
            draw.line(face_landmarks[facial_feature], width=5)

    # 결과 이미지를 새로운 폴더에 저장
    output_path = os.path.join(output_dir, image_file)
    pil_image.save(output_path)

print("모든 이미지 처리가 완료되었습니다.")
