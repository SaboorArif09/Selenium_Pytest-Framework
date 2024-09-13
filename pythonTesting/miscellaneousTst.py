from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options= chrome_options)

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
