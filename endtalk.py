from selenium import webdriver
driver = webdriver.Chrome('C:/Users/leo97/OneDrive - Personal/바탕 화면')
url = 'https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800'
driver.get(url)
xpath = "//table[@class='prettytable']//dd/a"
el_list = driver.find_elements_by_xpath(xpath)
print(el_list)
el_list2 = []
for i in el_list:
    el = i.text
    print(el)
    el_list[-1].text