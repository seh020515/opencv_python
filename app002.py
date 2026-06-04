#openCV 모듈 가져오기
import cv2

#버젼 확인
print(cv2.__version__)

## 이미지 불러와서 출력하기 https://www.pexels.com/ko-kr/ <무료이미지 사이트~
# img = cv2.imread('./res/img/sea.jpg') #이미지 읽기
# print(f'img shape {img.shape}')       #이미지 크기 (4000, 3000, 3) 세로 가로 색의갯수(BGR)
# img = cv2.resize(img, (300, 400))     #이미지 변경시 가로 세로
# cv2.imshow('title-seaImg', img)       #윈도우 이름, 출력할 이미지  #이미지 출력
# cv2.waitKey(0)                        #이미지가 5초동안 출력이 된다 / 단위 ms/0일시 키 누를때까지 기다림
# cv2.destroyAllWindows()               #모든 창 닫기

## 읽기 옵션
# imgColor = cv2.imread('./res/img/sea.jpg',cv2.IMREAD_COLOR) #bgr 유지
# imgColor = cv2.resize(imgColor, (300, 400))

# imgGRAY = cv2.imread('./res/img/sea.jpg',cv2.IMREAD_GRAYSCALE) #grayscale
# imgGRAY = cv2.resize(imgGRAY, (300, 400))

# imgUn = cv2.imread('./res/img/sea.jpg',cv2.IMREAD_UNCHANGED) #alpha 유지 (png투명도 유지 등)
# imgUn = cv2.resize(imgUn, (300, 400))

# cv2.imshow('title-imgColor', imgColor)
# cv2.imshow('title-imgGRAY', imgGRAY)
# cv2.imshow('title-imgUn', imgUn)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

## 동영상 불러와서 출력하기
# openCV에서 동영상을 불러온다는 것은 : 동영상 -> 프레임 추출 -> 이미지화 -> 출력

bakeMov = cv2.VideoCapture('./res/mov/bake.mp4')
while bakeMov.isOpened(): #동영상 파일이 연결되어 있다면
    result, frame = bakeMov.read() #result : read성공여부 ,frame : 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    #사이즈 조정
    frame = cv2.resize(frame, (300, 400))

    print(f'frame {frame}')
    cv2.imshow('title-bakeFrame', frame) #매우 빠르게 frame이 출력된다.
    
    if cv2.waitKey(1) == ord('q'): #1ms동안 기다린다. 사용자가 'q'를 입력하면 중단한다
        break

bakeMov.release() #외부 자원 해제
cv2.destroyAllWindows() #윈도우 창 닫기

#캠에서 동영상 실시간으로 불러오기 ^^
# bakeMov = cv2.VideoCapture(0)
# while bakeMov.isOpened(): #동영상 파일이 연결되어 있다면
#     result, frame = bakeMov.read() #result : read성공여부 ,frame : 받아온 이미지(프레임)
#     if not result:
#         print('END FRAME')
#         break

#     #사이즈 조정
#     frame = cv2.resize(frame, (300, 400))

#     print(f'frame {frame}')
#     cv2.imshow('title-bakeFrame', frame) #매우 빠르게 frame이 출력된다.
    
#     if cv2.waitKey(1) == ord('q'): #1ms동안 기다린다. 사용자가 'q'를 입력하면 중단한다
#         break

# bakeMov.release() #외부 자원 해제
# cv2.destroyAllWindows() #윈도우 창 닫기