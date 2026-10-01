# Singer.py

## 클래스 정의 : 가수
# 속성 : 이름, 성별, ...
# 동작/기능: 노래하기, 춤추기, ...

class Singer:
    # 1. 멤버변수(클래스/인스턴스) => 속성
    # 변수명 = 값
    iu_name = '아이유'
    bts_name = 'BTS'

    # 2. 메서드 => 동작
    def sing(self):
        print('이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~')
        # 인스턴스 멤버 변수
        self.gender1 = '여자'
        self.gender2 = '남자'
# 클래스 변수 접근: 클래스명.멤버변수명
print(Singer.iu_name)
print(Singer.bts_name)
## 객체 생성: 아이유, BTS, 오마이걸
iu = Singer()
bts = Singer()

## 객체 멤버 접근
iu.sing()
print(iu.gender1)
print(iu.iu_name)

bts.sing()
print(bts.bts_name)
print(bts.gender2)



# class Singer:
#     #클래스 멤버
#     name = "아이유"
#     gender = "여성"
#     group  = "여성 보컬"
    
#     def sing(self):
#         print("플레이리스트")
#         #인스턴스 멤버
#         self.songlist = \
#             "-밤편지 : 이 밤 그날의 반딧불을 당신의 창 가까이 보낼께요"
#         self.genre = "발라드"
# iu = Singer()
# bts = Singer()
# iu.sing()
# bts.sing()
# bts.genre = '발라드'
# bts.songlist = 'Dynamite'
# print(id(bts.genre) == id(iu.genre))
# print(id(bts.songlist) == id(iu.songlist))