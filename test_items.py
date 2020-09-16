def test_product_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    import time
    time.sleep(30)
    btest = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert btest, "Button not found"
