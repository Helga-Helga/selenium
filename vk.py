#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import lorem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print(os.environ['HOME'])

class PythonVKMessage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_send_message(self):
        driver = self.driver
        driver.get('https://vk.com')

        self.assertIn('Welcome!', driver.title)

        username = driver.find_element_by_id('index_email')
        username.clear()
        username.send_keys(os.environ['VK_LOGIN'])

        password = driver.find_element_by_id('index_pass')
        password.clear()
        password.send_keys(os.environ['VK_PASS'])

        login = driver.find_element_by_id('index_login_button')
        login.click()

        driver.implicitly_wait(20)
        messages = driver.find_element_by_xpath("//span[contains(text(), 'Сообщения')]")
        messages.click()

        driver.implicitly_wait(20)
        friend = driver.find_element_by_xpath("//*[contains(text(), 'user')]")
        friend.click()

        field = driver.find_element_by_id('im_editable0')
        field.clear()
        field.send_keys(lorem.sentence())
        field.send_keys(lorem.sentence(), Keys.ARROW_DOWN)
        field.send_keys(Keys.RETURN)

#smile = driver.find_element_by_xpath("//img[contains(@src,'/images/stickers/21/64.png')]")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
