from pages.demoqa import DemoQa
import time

from pages.elements_page import ElementsPage


def test_check_text(browser):
    # в файле test_check_text.py реализуйте тест кейс:
    # a.перейти на страницу 'https://demoqa.com/'
    # b.проверить что текст в подвале == '© 2013 - 2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    # в файле test_check_text.py реализуйте тест кейс:
    # a.перейти на страницу 'https://demoqa.com/'
    # b.через кнопку перейти на страницу 'https://demoqa.com/elements'
    # c.проверить что текст по центру == 'Please select an item from left to start practice.'
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    time.sleep(5)
    assert demo_qa_page.center.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()
