 > [!abstraction] 
 > Python 에서도 inheritance, polymorphism, and encapsulation을 제공한다.

<br />


### Item 37: Compose Classes Instead of Nesting Many Levels of Built-in Types
---

 > [!info] 
 > - Python의 딕셔너리 타입은 동적으로 객체의 생명주기 동안 내부 상태를 관리하는데 꽤 좋다.
 > - 미리 정의된 속성 값을 사용해서 각 학생을 표현하지 않고 Dictionary 타입을 사용해서 표현해 보자
 
 > [!explain] Dictionary 타입을 사용해서  _grades를 정의
```python
class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)
        
	def print_grades(self, name):
      for _, grade in enumerate(self._grades[name]):
          print(colored(f'grade : {grade}', 'green'))


```

 > [!explain] 클라이언트 에서 사용
```python
def print_simpleGradeBook():
    book = SimpleGradebook()
    book.add_student('Issac Newton')
    book.report_grade('Issac Newton', 90)
    book.report_grade('Issac Newton', 95)
    book.report_grade('Issac Newton', 85)
    book.print_grades('Issac Newton') 


if __name__ == '__main__':
    print_simpleGradeBook()
```

 > [!info] 
 > - 딕셔너리 및 연관된 빌트인 타입들은 사용하기는 쉽지만 과도한 확장으로 인해 다루기 힘든 코드를 작성할 수 있는 위험이 있다.
 > - 예를 들어 SimpleGradebook 클래스에서 과목 별 점수 형태로 관리하도록 기능을 확장한다고 하자.
 > - 기존과 다르게 `_grade` 딕셔너리가 학생 이름 별로 다른 형태의 딕셔너리를 가리키도록 변경해야 한다.
 > - 이전 chapter 에서 본 것과 같이 `defaultdict`를 써보자.
 
```python
from collections import defaultdict
class BySubjectGradebook:
    def __init__(self):
		self._grades = {}           # Outer dict
        
    def add_student(self, name):
        self._grades[name] = defaultdict(list)  # Inner dict

```