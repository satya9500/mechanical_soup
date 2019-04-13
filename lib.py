import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

browser.open("http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fW27%2fMyInfo%2fw27MyInfo.aspx")


browser.select_form('form[action="login.aspx?ReturnUrl=%2fW27%2fMyInfo%2fw27MyInfo.aspx"]')
browser["txtUserName"] = "18178"
browser["Password1"] = "MEMBER"
browser.submit_selected()

print(browser.get_url())