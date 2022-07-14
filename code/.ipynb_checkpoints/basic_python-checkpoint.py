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

# +
# ----- list, set -----
# set 연산 [https://dojang.io/mod/page/view.php?id=2315](https://dojang.io/mod/page/view.php?id=2315)
# 파이썬 기본 연산자의 시간복잡도 [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=221204308911](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=221204308911)
# -

# 임의의 리스트
l = ['a','bb','ccc','dddd']

# 리스트 원소 삭제
l.remove('ccc')
l

# 리스트에 원소 삽입
l.insert(3, 'a')
l

# 리스트에서 특정값의 인덱스 찾기
l.index('a')

# 문자로 이루어진 리스트를 문자열로 변환
''.join(l)

# 리스트 원소 정렬
l.sort(reverse=True) # reverse는 역순
l

l.sort(key=len) # 원소 길이순 정렬
l

# 리스트 중복 제거 및 정렬
list(set(l))

# 겹치는 원소 삭제
l1 = [1,2,3,4]
l2 = [2,3,4]
set(l1) - set(l2)

# +
# ----- enumerate -----
# -

l = ['a', 'b', 'c']
d = {str(l[idx]): idx+1 for idx, q in enumerate(l)}
d

d.items() 

# +
# ----- zip -----
# -

for i, j in zip(d.items(), d.items()):
    print(i, j)


# +
def main(a, b, c):
    sub_list = map(list, zip(b, c))
    return dict(zip(a, sub_list))

a = ['first', 'second']
b = [1,2]
c = [3,4]

main(a, b, c)

# +
# ----- formatting -----
# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=ksg97031&logNo=221126216595&parentCategoryNo=&categoryNo=62&viewDate=&isShowPopularPosts=true&from=search
# -

'stnd_ymd={0}'.format('2022-06-08')

# +
# ----- global -----

# +
x = 10

def func():
    global x # 이거 안쓰면 에러남 ('UnboundLocalError: local variable 'x' referenced before assignment')
    x += 1
    print(x)

func()

# +
global_var = 10

class LocalClass:
    
    def global_add(self, num):
        
        global global_var # 이거 안쓰면 에러남 ('UnboundLocalError: local variable 'global_var' referenced before assignment')
        global_var = global_var + num
        print(global_var)

        
localclass = LocalClass()
localclass.global_add(10)

# +
# ----- if ~ continue -----
# 조건을 만족하는 경우 아래 코드를 지나침
# -

for i in range(10):       
    if i % 2 == 0:         
        continue           
    print(i)

# +
# ----- try, except -----

# +
a = 10
b = 0

try:
    print(a/b)
    
except Exception as e: # 에러메시지 출력
    print(e) 

# +
# 특정 에러에 대한 출력
y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)

except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')

except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')

# +
# ----- 함수 -----
# -

# : 뒤에 input의 자료형 표시
# = 뒤에 default값 표시
'''def myfunction(input1, input2: str, input3=[], input4=10):
    ~~'''


# +
# ----- yield, generator -----
# https://github.com/yeomko22/python_study/blob/master/week1_generator.ipynb
# generator는 모든 값을 메모리에 담고 있지 않고 그때그때 값을 생성(generator)해서 반환. 대용량 반복을 수행해야할 때, 메모리를 더욱 효율적으로 사용하도록 함
# yield를 호출하면 원하는 값을 리턴하며, 실행 흐름을 일시 정지하여 함수를 재활용할 수 있는 상태로 만듦
# return 키워드를 사용할 때는 모든 결과 값을 메모리에 올려놓아야 하는 반면에, yield 키워드를 사용할 때는 결과 값을 하나씩 메모리에 올려놓음

# +
# return 예시
def myfunction():
    
    total = 5
    current = 0
    
    while current < total:
        current += 1
        return current # return이 호출되면 반복을 멈추고, 수를 반환
        print('hello')
    
myfunction()


# +
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
# -








