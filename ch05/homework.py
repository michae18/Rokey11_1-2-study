# homework.py

# 1번 for문의 실행 결과를 예측하라.
# 과일s = ['사과', ' 귤', '수박']
# for 과일 in 과일s:
#     print(과일)

# 2번 다음 코드를 for문으로 작성하라.
# for num in range(1,4):
#     n = 10
#     num = num * n
#     print(num)

# 3번 다음과 같이 상품 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 
# for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
# price_list = [100,200,300]
# add_price = 10
# for price in price_list:
#     t_price = price + add_price
#     print(t_price)

# 4번 리스트에는 동물이름이 문자열로 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라. dog3\n cat3\n parrot6
# ani_list = ['dog', 'cat', 'parrot']
# for ani_name in ani_list:
#     name_len = len(ani_name)
#     print(ani_name,'',name_len)
     

# 5. 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 나
# 다
# 라

# ko_list = ['가','나','다','라']
# for ko in ko_list:
#     if ko != '가':
#         print(ko)

# 6. 리스트에는 네 개의 정수가 저장돼 있다.
# 리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
# nums = [3, -20, -3, 44]
# for num in nums :
#     if num < 0:
        # print(num)

# 7. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 
# 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# for year in range(2002,2051,4):
#     print(year)

# 9. while문을 사용하여 1부터 100까지의 자연수를 모두 더하고 그 결과를 출력하시오.
# num_sub = 0
# num = 0
# while num <= 100 :
#     num_sub += num
#     num += 1
# print(num_sub) 

# 10. 1부터 30까지의 정수를 홀수와 짝수를 구분하여 출력하시오.
# for num in range(31):
#     if num % 2 != 0:
#         print(num,' : 홀수')
#     else :
#         print(num,' : 짝수')

# 11. 앞선 프로그램을 수정하여 홀수와 짝수를 구분하여 리스트에 저장하고 출력 하시오.
hol_num =[]
jjack_num = []
for num in range(31):
    if num % 2 != 0:
        hol_num.append(num)
    else :
        jjack_num.append(num)
print(hol_num)
print(jjack_num)

