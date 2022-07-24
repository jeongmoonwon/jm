# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
# 파이썬 버전 확인하기
import sys
print(sys.version)

# + pycharm={"name": "#%%\n"}
# ----- list, set -----
# set 연산 [https://dojang.io/mod/page/view.php?id=2315](https://dojang.io/mod/page/view.php?id=2315)
# 파이썬 기본 연산자의 시간복잡도 [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=221204308911](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=221204308911)

# + pycharm={"name": "#%%\n"}
# 임의의 리스트
l = ['a','bb','ccc','dddd']

# + pycharm={"name": "#%%\n"}
# 리스트 원소 삭제
l.remove('ccc')
l

# + pycharm={"name": "#%%\n"}
# 리스트에 원소 삽입
l.insert(3, 'a')
l

# + pycharm={"name": "#%%\n"}
# 리스트에서 특정값의 인덱스 찾기
l.index('a')

# + pycharm={"name": "#%%\n"}
# 문자로 이루어진 리스트를 문자열로 변환
''.join(l)

# + pycharm={"name": "#%%\n"}
# 리스트 원소 정렬
l.sort(reverse=True) # reverse는 역순
l

# + pycharm={"name": "#%%\n"}
l.sort(key=len) # 원소 길이순 정렬
l

# + pycharm={"name": "#%%\n"}
# 리스트 중복 제거 및 정렬
list(set(l))

# + pycharm={"name": "#%%\n"}
# 겹치는 원소 삭제
l1 = [1,2,3,4]
l2 = [2,3,4]
set(l1) - set(l2)

# + pycharm={"name": "#%%\n"}
# ----- enumerate -----

# + pycharm={"name": "#%%\n"}
l = ['a', 'b', 'c']
d = {str(l[idx]): idx+1 for idx, q in enumerate(l)}
d

# + pycharm={"name": "#%%\n"}
d.items() 

# + pycharm={"name": "#%%\n"}
# ----- iter, next -----

# + pycharm={"name": "#%%\n"}
L_list = [1,2,3,4,5]

# for문과 비교
for index in L_list: # Automatic iteration 
    print(index)  

# + pycharm={"name": "#%%\n"}
I = iter(L_list)
print(next(I))  
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I))
print(next(I)) # 더 이상 가져올 게 없으면 에러

# + pycharm={"name": "#%%\n"}
print(next(I,20)) # 기본값을 지정하면 반복이 끝나더라도 기본값 출력

# + pycharm={"name": "#%%\n"}
# ----- zip -----

# + pycharm={"name": "#%%\n"}
for i, j in zip(d.items(), d.items()):
    print(i, j)


# + pycharm={"name": "#%%\n"}
def main(a, b, c):
    sub_list = map(list, zip(b, c))
    return dict(zip(a, sub_list))

a = ['first', 'second']
b = [1,2]
c = [3,4]

main(a, b, c)

# + pycharm={"name": "#%%\n"}
# ----- formatting -----
# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=ksg97031&logNo=221126216595&parentCategoryNo=&categoryNo=62&viewDate=&isShowPopularPosts=true&from=search

# + pycharm={"name": "#%%\n"}
'stnd_ymd={0}'.format('2022-06-08')

# + pycharm={"name": "#%%\n"}
# ----- global -----

# + pycharm={"name": "#%%\n"}
x = 10

def func():
    global x # 이거 안쓰면 에러남 ('UnboundLocalError: local variable 'x' referenced before assignment')
    x += 1
    print(x)

func()

# + pycharm={"name": "#%%\n"}
global_var = 10

class LocalClass:
    
    def global_add(self, num):
        
        global global_var # 이거 안쓰면 에러남 ('UnboundLocalError: local variable 'global_var' referenced before assignment')
        global_var = global_var + num
        print(global_var)

        
localclass = LocalClass()
localclass.global_add(10)

# + pycharm={"name": "#%%\n"}
# ----- if ~ continue -----
# 조건을 만족하는 경우 아래 코드를 지나침

# + pycharm={"name": "#%%\n"}
for i in range(10):       
    if i % 2 == 0:
        print('exception')
        continue           
    print(i)

# + pycharm={"name": "#%%\n"}
# ----- try, except -----

# + pycharm={"name": "#%%\n"}
a = 10
b = 0

try:
    print(a/b)
    
except Exception as e: # 에러메시지 출력
    print(e) 

# + pycharm={"name": "#%%\n"}
# 특정 에러에 대한 출력
y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)

except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')

except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')

# + pycharm={"name": "#%%\n"}
# ----- 함수 -----

# + pycharm={"name": "#%%\n"}
# : 뒤에 input의 자료형 표시
# = 뒤에 default값 표시
'''def myfunction(input1, input2: str, input3=[], input4=10):
    ~~'''


# + pycharm={"name": "#%%\n"}
# ----- yield, generator -----
# https://github.com/yeomko22/python_study/blob/master/week1_generator.ipynb
# generator는 모든 값을 메모리에 담고 있지 않고 그때그때 값을 생성(generator)해서 반환. 대용량 반복을 수행해야할 때, 메모리를 더욱 효율적으로 사용하도록 함
# yield를 호출하면 원하는 값을 리턴하며, 실행 흐름을 일시 정지하여 함수를 재활용할 수 있는 상태로 만듦
# return 키워드를 사용할 때는 모든 결과 값을 메모리에 올려놓아야 하는 반면에, yield 키워드를 사용할 때는 결과 값을 하나씩 메모리에 올려놓음
# 리스트에 함수를 적용하는 경우 yield가 더 빠름

# + pycharm={"name": "#%%\n"}
# return 예시
def myfunction():
    
    total = 5
    current = 0
    
    while current < total:
        current += 1
        return current # return이 호출되면 반복을 멈추고, 수를 반환
        print('hello')
    
myfunction()


# + pycharm={"name": "#%%\n"}
# yield 예시
def myfunction():
    total = 5
    current = 0
    
    while current < total:
        current += 1
        yield current # yield가 호출되면 함수는 그 시점에서 일시 정지
        print('hello')
        
yield_result = myfunction()
print(yield_result)
print(next(yield_result)) # next()를 통해 yield 바로 다음 라인부터 다시 실행을 이어나감
print(next(yield_result))
print(next(yield_result))
# + pycharm={"name": "#%%\n"}
# ----- 텍스트 -----

# + pycharm={"name": "#%%\n"}
x1 = 'abc'
x2 = '123'

# + pycharm={"name": "#%%\n"}
# 숫자로만 이루어진 문자열인지 여부를 확인
x1.isdigit()

# + pycharm={"name": "#%%\n"}
x2.isdigit()


# + pycharm={"name": "#%%\n"}
# 알파벳으로만 이루어진 문자열인지 여부를 확인
x1.isalpha()

# + pycharm={"name": "#%%\n"}

