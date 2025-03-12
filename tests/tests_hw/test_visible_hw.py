from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.section_content.visible()
    accordion_page.section_heading.click()
    time.sleep(2)
    assert not accordion_page.section_content.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.content_elem_first.visible()
    assert not accordion_page.content_elem_second.visible()
    assert not accordion_page.content_elem_third.visible()