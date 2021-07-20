#pandas 라이브러리 불러오기
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib 은 데이터 시각화 라이브러리이다. plot()을 이용하여 그래프를 그릴 수 있다.

# read_csv() 매서드로 train.csv 파일을 df class 로 불러오기.
train = pd.read_csv('와인/train.csv')

# info() 매서드로 데이터의 정보를 확인. 
# info() 매서드를 활용하여 데이터의 피쳐수와 컬럼명, 결측치여부, Dtype 에 대한 정보를 알 수 있다.
train.info()

# shape 어트리뷰트로 행, 열을 파악.
# shape 어트리뷰트를 쓰면 데이터의 행갯수, 열갯수를 출력해 데이터의 크기를 파악할 수 있다.
train.shape

# head() 매서드로 데이터의 각 컬럼의 정보를 조사.
#head() 매서드를 통해 데이터의 대략적인 정보를 알 수 있다.
train.head()

train = pd.read_csv('와인/train.csv')
test = pd.read_csv('와인/test.csv')

# isnull() 매서드로  결측치 존재여부를 확인
train.isnull()
test.isnull()

# sum() 매서드로 결측치의 갯수를 출력
train.isnull().sum()

test.isnull().sum()

# describe() 메서드는 다양한 통계량을 요약해주는 굉장히 편리한 메소드이다

# DataFrame에 describe() 메서드를 실행시키면 각 열에 대해 요약이 수행된다 

# 결측치는 제외하고 수치형 데이터에 한해 데이터 요약이 수행된다

# 기본적으로 count, mean, std, min , 1 분위수, 2 분위수, 3 분위수, max 값이 출력된다

train.describe()
print("describe->", train.describe())

# x축 지점의 값들로 정할 리스트를 생성.
x_values = [0, 1, 2, 3, 4]

# y축 지점의 값들
y_values = [0, 1, 4, 9, 16]

# line 그래프를 그린다
plt.plot(x_values, y_values)

# 그래프를 화면에 보여준다
plt.title("Line Graph")
plt.show()

# 히스토그램 (Histogram) 은 도수분포표를 그래프로 나타낸 것 . 변수들의 분포정도를 볼 때 유용하다.

# 변수 분포를 갖는 리스트를 생성.
a = [1,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,7]

# line 그래프를 그린다
plt.hist(a)

# 그래프(막대)를 화면에 보여준다
plt.title("Histogram")
plt.show()

# 글꼴 설정
plt.rc('font', family='NanumBarunGothic')

# 마이너스 기호 출력
plt.rc('axes', unicode_minus=False)

# 분석에 문제가 없는 경고 메세지는 숨긴다.
import warnings
warnings.filterwarnings('ignore')

train = pd.read_csv('와인/train.csv')

# copy() 매서드로 학습 데이터의 복사본을 생성.
# 시각화를 진행할 때는 보통 copy() 매서드로 복사본을 생성한 후 진행한다.
traindata = train.copy()

# 타깃 변수(와인 품질) 분포 시각화
# seaborn 의 distplot() 매서드를 이용
sns.distplot(traindata['quality'], kde=False, bins=10)

# matplotlib 의 axis() 매서드로 그래프 축의 최솟값, 최댓값을 지정할 수 있다.
plt.axis([0, 10, 0, 2500]) # [x 축 최솟값, x 축 최댓값, y 축 최솟값, y 축 최댓값]

# matplotlib 의 title() 매서드로 그래프의 제목을 지정할 수 있다.
plt.title("Wine Quality ") # 그래프 제목 지정

# matplotlib 의 show() 매서드로 그래프를 출력할 수 있다.
plt.show() # 그래프 그리기