from selenium import webdriver

url = 'https://www.youtube.com/watch?v=bQbv8r7i7L0'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
