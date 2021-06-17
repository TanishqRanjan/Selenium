from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
import time


from selenium.webdriver.support.select import Select

wd = webdriver.Chrome(executable_path="C:\\Users\\Hp\\webdriver\\chromedriver_win32\\chromedriver.exe")

print(wd.title)
print(wd.current_url)
wd.get("https://www.thesparksfoundationsingapore.org/join-us/internship-positions/")
print("\nTest Cases")


print("\nTestCase 1:")
if wd.title:
    print("\nTitle Verified Successfully:", wd.title)
else:
    print("\nTitle Verification Failed:\n")

print("\nTestCase 2:")

try:
    wd.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Success! The logo is present\n')
    time.sleep(2)
except NoSuchElementException:
    print('No logo is present!\n')

print("TestCase3:")
try:
    wd.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed\n")

print("Test case 4:")
try:
    wd.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home Link is working!\n")
except NoSuchElementException:
    print("Home Link Doesn'tWork!\n")


print("TestCase 5:")
try:
    wd.find_element_by_link_text('About Us').click()
    time.sleep(2)
    wd.find_element_by_link_text('Corporate Partners').click()
    time.sleep(2)
    print("Page visited Successfully!\n")
except NoSuchElementException:
    print("Page visit Failed! Does not exist./n")
    time.sleep(2)

# Test case 6 : Policy Page
print("TestCase 6:")
try:
    wd.find_element_by_link_text('Policies and Code').click()
    time.sleep(2)
    wd.find_element_by_link_text("Policies").click()
    time.sleep(2)
    wd.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(2)
    print("Policy Page Verification:\n")

except NoSuchElementException:
    print("No New Tab opened!\n")

# Test Case 7:: Program Page
print('Test Case 7:')
try:
    wd.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(2)
    wd.find_element_by_link_text('Student Mentorship Program').click()
    time.sleep(2)
    wd.find_element_by_link_text('Student SOS Program').click()
    time.sleep(2)
    print('Program Page Is Verified\n')
except NoSuchElementException:
    print('No new Tab is opened\n')

    # TestCase 8: Check the contact us page
print("TestCase 8:")
try:
    wd.find_element_by_link_text('Contact Us:').click()
    time.sleep(2)
    info = wd.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]/h4')
    time.sleep(2)

    # print(Info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Correct!')

    print("Contact Page Verification Successful!")
except NoSuchElementException:
    print("Contact Page verification Unsuccessful!")


# Test Case 9:
print("TestCase 9:")
try:
    wd.find_element_by_link_text('LINKS').click()
    time.sleep(2)
    wd.find_element_by_link_text('Software & App').click()
    time.sleep(2)
    wd.find_element_by_link_text('AI in Education').click()
    time.sleep(2)
    print('Link verification Successful!\n')
except NoSuchElementException:
    print("Link Verification Failed!\n")

# TestCase 10: Check The From

print("TestCase 10:")
try:
    wd.find_element_by_link_text('Join Us').click()
    time.sleep(2)
    wd.find_element_by_link_text('Why Join Us').click()
    time.sleep(2)
    wd.find_element_by_name('Name').send_keys('Tanishq ranjan')
    time.sleep(2)
    wd.find_element_by_name('Email').send_keys('Sahtanishq123@gmail.com')
    select = Select(wd.find_element_by_class_name('form-control'))
    time.sleep(2)
    select.select_by_visible_text('Intern')
    time.sleep(2)
    wd.find_element_by_class_name('button-w3layouts').click()
    time.sleep(2)
    print("From Verification Successful!\n")
except NoSuchElementException:
    print("From Verification Failed!\n")
    time.sleep(2)

cls = wd.close()



