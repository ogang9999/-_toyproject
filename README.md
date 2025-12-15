toy_project
폴더 구조
project/
 ├─ pygame_images/
 │   ├─ background.png
 │   ├─ stage.png
 │   ├─ character.png
 │   ├─ weapon.png
 │   ├─ ball_1.png
 │   ├─ ball_2.png
 │   ├─ ball_3.png
 │   └─ ball_4.png
 │
 ├─ toy_project.py(게임 실행 파일)
 ├─ README.md

1) 본 프로젝트는 Python의 pygame 라이브러리를 활용하여 제작한 간단한 2D 액션 게임입니다.
   플레이어는 좌우로 이동하며 무기를 발사하여 떨어지는 공을 제안시간 내에 부수는 것이 목표입니다.
   공은 맞을수록 더 작은 공으로 분리되며, 모든 공을 제거하면 게임이 종료됩니다.

2) 본 프로그램은
..이벤트 처리
..충돌 감지
..객체 분리 로직
..프레임 기반 애니메이션
등을 직접 구현해보는 것을 목표로 기획되었습니다.
특히 공이 충돌 시 좌우로 분리되는 구조를 통해 게임 로직 설계에 집중하였습니다
 또한 게임에서 사용되는 이미지 셋들은 AI(ChatGPT, Nono Banana)를 통해 만들었습니다.

4) 주요 기능
키보드 입력을 통한 캐릭터 이동 (← / →)
스페이스바를 이용한 무기 발사
무기와 공의 충돌 감지
공이 맞을 경우 더 작은 공으로 분리
제한 시간 시스템
게임 클리어 / 게임 오버 처리

5) 실행 방법
 toy_project.py 을 열고
 이후 터미널(ctrl+`)을 통해 pygame이라는 외부 패키지를 설치
  (pip install pygame 또는 python -m pip install pygame 또는 python3 -m pip install pygame)
 그 다음 파일을 실행하시면 됩니다.

6) 조작 방법
| 키     | 기능     |
| ----- | ------ |
| ← / → | 캐릭터 이동 |
| Space | 무기 발사  |

6. 실행 화면
▶ 게임 시작 화면
<img width="1280" height="1016" alt="screenshot_1" src="https://github.com/user-attachments/assets/edc86fe3-2552-420c-8893-b09ae3ac5ccb" />

▶ 플레이 화면
<img width="1268" height="1020" alt="screenshot_2" src="https://github.com/user-attachments/assets/42389307-515b-478b-80d0-a3cc806d351c" />


 
