from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

# 그녀는 바로 작업을 추가 하기로 한다.

# "공작깃털 사기"라고 텍스트 상자를 입력한다.
# (에디스의 취미는 날치잡이용 그물을 만드는 것이다.)

# 엔터키를 치면 페이지가 갱신되고 작업목록에
# "1: 공작깃털 사기" 아이템이 추가된다.

# 추가 아이템을 입력할 수 있는 여분의 텍스트상자가 존재한다.
# 다시 "공작 깃털을 이용해서 그물만들기"라고 입력한다 (에디스는 매우 체계적인 사람이다)

# 페이지는 다시 갱신되고, 두개 아이템이 목록에 보인다.

# 만족하고, 잠자리에 든다.

browser.quit()