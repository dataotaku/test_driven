from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # 에디스는 좋은 온라인 To-Do 앱이 있다는 소식을 들었다.
        # 해당 웹사이트에 확인하러간다.
        self.browser.get("http://localhost:8000")

        # 웹페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # 그녀는 바로 작업을 추가 하기로 한다.
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # "공작깃털 구매"라고 텍스트 상자를 입력한다.
        # (에디스의 취미는 날치잡이용 그물을 만드는 것이다.)
        inputbox.send_keys("Buy peacock feathers")

        # 엔터키를 치면 페이지가 갱신되고 작업목록에
        # "1: 공작깃털 사기" 아이템이 추가된다.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows))

        # 추가 아이템을 입력할 수 있는 여분의 텍스트상자가 존재한다.
        # 다시 "공작 깃털을 이용해서 그물만들기"라고 입력한다 (에디스는 매우 체계적인 사람이다)
        self.fail("Finish the test!")

        # 페이지는 다시 갱신되고, 두개 아이템이 목록에 보인다.

        # 만족하고, 잠자리에 든다.

if __name__ == "__main__":
    unittest.main()