from selenium import webdriver
import time
import random

driver = webdriver.Chrome("chromedriver.exe")
trial = 0

def login():
    driver.get("https://nid.naver.com/nidlogin.login?url=https://v-search.nid.naver.com/reservation?orgCd%3D12335843%26sid%3D31059094")


def load_map():
    driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used")
    time.sleep(7)
    here = driver.find_element_by_class_name('_3_X4H._1dUVm')
    here.click()
    time.sleep(5)
    list_button = driver.find_element_by_class_name("_31ySW ")
    list_button.click()
    time.sleep(5)
    print("Get Ready For Vaccine Crawling")


def update():
    try:
        time.sleep(random.random() / 2)
        update_button = driver.find_element_by_class_name("_1MCHh")
        update_button.click()
        while update_button.get_attribute('class') != "_1MCHh":
            time.sleep(0.05)
        return True
    except:
        return False


def is_there_vaccine():
    try:
        get_vaccine = driver.find_element_by_xpath('//*[@id="_list_scroll_container"]/div/div/div[3]/ul/li/div[2]/div[1]/a')
        get_vaccine.click()
        print("Vaccine Found!")
        print("   " + str(time.ctime()))
        return True
    except:
        return False


def reservation():
    clicked = False
    for i in range(1):
        try:
            reservation_button = driver.find_element_by_xpath('//*[@id="reservation_confirm"]')
        except:
            pass
        reservation_button.click()
        clicked = True
        print("Reservation Button Clicked")
        print("   " + str(time.ctime()))
    return clicked


def give_me():
    while True:
        load_map()
        for i in range(300):
            if not update():
                continue;
            if is_there_vaccine():
                if reservation() == True:
                    trial += 1
                    time.sleep(2)
                    driver.get_screenshot_as_file(str(trial) + ".png")
                    time.sleep(3)
                    print("Screenshot Saved")
                    print("   " + str(time.ctime()))


def one_hospital(key='JUnxTruwhXPbf6M'):
    while True:
        driver.get('https://v-search.nid.naver.com/reservation/info?key=' + key)
        is_there_vaccine_one_hospital()
        try:
            driver.find_element_by_xpath('//*[@id="reservation_confirm"]')
        except:
            trial += 1
            driver.get_screenshot_as_file(str(trial) + ".png")
            time.sleep(2)
            print("Screenshot Saved")
            print("   " + str(time.ctime()))


def is_there_vaccine_one_hospital():
    while True:
        try:
            reservation_button = driver.find_element_by_xpath('//*[@id="reservation_confirm"]')
        except:
            time.sleep(0.01)
        reservation_button.click()
        break


login()


