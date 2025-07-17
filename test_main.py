from selene import browser, be, have


def test_search_with_results(browser_settings):
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text("Selene: User-Oriented Web UI Browser Tests in Python "))


def test_search_without_results(browser_settings):
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('fgdfgdfgdfdвквп').press_enter()
    browser.element('html').should(have.text("По запросу «fgdfgdfgdfdвквп» ничего не найдено."))

