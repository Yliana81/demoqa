from pages.modal_dialogs import ModalDialogsPage
from pages.demoqa import DemoQa

# Домашнее задание №9
# 1. создайте тестовый файл test_page_dialogs.py реализуйте тест кейс test_modal_elements()
# a. перейти на страницу https://demoqa.com/modal-dialogs
# i. в каталоге pages создайте класс страницы modal_dialogs.py
# ii. в тестовом файле создайте объект новой страницы
# iii. от объекта вызовите метод входа на страницу
# b. проверить, что кнопок подменю, на странице - 5 шт
# i. в классе страницы создайте элемент с не уникальным локатором, подходящим под все кнопки
# ii. в тестовом файле обратитесь к объекту страницы - к элементу - вызовите метод проверки кол-ва элементов
# 2. в том-же файле реализуйте тест кейс test_navigation_modal()
# a. перейти на страницу https://demoqa.com/modal-dialogs
# i. класс страницы уже создан
# ii. создайте объект новой страницы
# iii. от объекта вызовите метод входа на страницу
# b. обновить страницу
# c. перейти на главную страницу через иконку
# i. в файле класса страницы создайте элемент иконки
# d. сделать шаг назад стрелкой браузера
# e. установить размеры экрана 900х400
# f. сделать шаг вперед стрелкой браузера
# g. вызвать проверку урла на главной странице
# h. проверить title на главной
# i. вернуть размеры экрана по умолчанию 1000x1000

def test_modal_elements(browser):
    elements_page = ModalDialogsPage(browser)
    elements_page.visit()
    assert elements_page.alerts_frame_win_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    elements_page = ModalDialogsPage(browser)
    first_page = DemoQa(browser)
    elements_page.visit()
    elements_page.refresh()
    elements_page.icon_first.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert first_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
