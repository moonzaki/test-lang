def test_product_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    import time
    time.sleep(5)
    btest = browser.find_elements_by_css_selector('button.btn:nth-child(3)')
    assert btest != 0, "Button not found"