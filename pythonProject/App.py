from PagePattern import SearchHelper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

UserInfo = {"FN": "Dima",
            "SN": "Dima",
            "Email": "dima_miel7nichien6ko5@mail.ru",
            "Password": "qwerty"
            }
#registration
def test_main_registration(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    RegButton = Medicine_main_page.get_element_by_class("ico-register")
    #print(RegButton.get_text())
    RegButton.click()
    Gender = Medicine_main_page.get_element_by_ID("gender-male")
    FN = Medicine_main_page.get_element_by_ID("FirstName")
    SN = Medicine_main_page.get_element_by_ID("LastName")
    Email = Medicine_main_page.get_element_by_ID("Email")
    Password = Medicine_main_page.get_element_by_ID("Password")
    ConfPassword = Medicine_main_page.get_element_by_ID("ConfirmPassword")
    Gender.click()
    FN.send_keys(UserInfo["FN"])
    SN.send_keys(UserInfo["SN"])
    Email.send_keys(UserInfo["Email"])
    Password.send_keys(UserInfo["Password"])
    ConfPassword.send_keys(UserInfo["Password"])
    ConfPassword.send_keys(Keys.RETURN)
    result = Medicine_main_page.get_element_by_class("validation-summary-errors")
    if result is not None:
        print(" =Already exsist")

    time.sleep(2)
    result = Medicine_main_page.get_element_by_class("result")
    if result is not None:
        print(" =Successfully registered")
    else:
        print("Something went")
#login
def test_main_login(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    LogButton = Medicine_main_page.get_element_by_class("ico-login")
    LogButton.click()
    Email = Medicine_main_page.get_element_by_ID("Email")
    Password = Medicine_main_page.get_element_by_ID("Password")
    Email.send_keys(UserInfo["Email"])
    Password.send_keys(UserInfo["Password"])
    Password.send_keys(Keys.RETURN)
    time.sleep(2)
    result = Medicine_main_page.get_element_by_class("account")
    if result is not None:
        print("Successfully log in")
    else:
        print("Something went")
#navigation_menu
Menu_array_titles = ['Books','Computers','Electronics','Apparel & Shoes','Digital downloads','Jewelry','Gift Cards']
Menu_array_links = ['/books','/computers','/electronics','/apparel-shoes','/digital-downloads','/jewelry','/gift-cards']
def test_main_navigation_FindBook(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    elements = Medicine_main_page.check_navigation_bar(".top-menu li")
    assert 'BOOKS' in elements
def test_main_navigation_FindHi(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    elements = Medicine_main_page.check_navigation_bar(".top-menu li")
    assert 'Hi' in elements
def test_main_navigation_CheckLinks(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    for i in range(len(Menu_array_titles)):
        Element = Medicine_main_page.get_element_by_link(Menu_array_links[i])
        Element.click()
        time.sleep(1)
        if Medicine_main_page.get_element_by_class("page-title").text != Menu_array_titles[i]:
            raise Exception("This isn't this page title")
#search
FindProduct = "Camcorder"
link = "/camcorder"
def test_main_search_product(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    Search_input = Medicine_main_page.get_element_by_ID("small-searchterms")
    Search_input.send_keys(FindProduct)
    Search_input.send_keys(Keys.RETURN)
    time.sleep(1)

    Element = Medicine_main_page.get_element_by_link(link)
    Element.click()
    time.sleep(2)

    if Medicine_main_page.get_element_by_class("product-name").text != (FindProduct):
        raise Exception("Another product")
#filter
def test_main_sort(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    Element = Medicine_main_page.get_element_by_link(Menu_array_links[0])
    Element.click()
    element_sort = Medicine_main_page.get_element_by_ID("products-orderby")
    selector = Select(element_sort)
    selector.select_by_index(3)

    #Price_array = Medicine_main_page.get_elements_by_class("price actual-price")
    Price_array = Medicine_main_page.get_elements_by_class("actual-price")
    for i in range(1,len(Price_array)):
        if Price_array[i-1].text > Price_array[i].text:
            raise Exception("Not sorted")
#add to bin
def test_main_buy(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    Element = Medicine_main_page.get_element_by_link(Menu_array_links[0])
    Element.click()

    Product = Medicine_main_page.get_elements_by_class("product-title")
    name_product = Product[0].text
    Product[0].click()
    time.sleep(1)
    Add_to_card = Medicine_main_page.get_element_by_class("add-to-cart-button")
    Add_to_card.click()
    time.sleep(1)
    bin_button = Medicine_main_page.get_element_by_class("cart-label")
    bin_button.click()
    time.sleep(1)
    Name_in_bin = Medicine_main_page.get_element_by_class("product-name").text

    if Name_in_bin != (name_product):
        raise Exception("Not a valid product name")
#bin_moves
def test_main_update_bin(main_open):
    Medicine_main_page = SearchHelper(main_open)
    Medicine_main_page.go_to_site()
    Element = Medicine_main_page.get_element_by_link(Menu_array_links[0])
    Element.click()

    Product = Medicine_main_page.get_elements_by_class("product-title")
    Product[0].click()
    time.sleep(1)
    Add_to_card = Medicine_main_page.get_element_by_class("add-to-cart-button")
    Add_to_card.click()
    time.sleep(1)
    bin_button = Medicine_main_page.get_element_by_class("cart-label")
    bin_button.click()
    time.sleep(1)
    product_price = Medicine_main_page.get_element_by_class("product-unit-price").text
    qty = Medicine_main_page.get_element_by_class("qty-input")
    qty.clear()
    qty.send_keys("4")
    update_button = Medicine_main_page.get_element_by_class("update-cart-button")
    update_button.click()
    Total_price = float(Medicine_main_page.get_element_by_class("product-subtotal").text)
    price = float(product_price)  * 4

    if price != Total_price:
        raise Exception(str(price) +" is not equal to "+Total_price)

