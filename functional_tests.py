from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'./geckodriver-v0.30.0-win64/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
