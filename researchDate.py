#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv



browser = webdriver.Chrome()
browser.get()
sleep(2)

username = browser.find_element_by_id()
username.send_keys()
submit_button = browser.find_element_by_id()
submit_button.submit()
sleep(2)

password = browser.find_element_by_id()
password.send_keys()
submit_button.submit()
sleep(3)

print('ログイン成功')

cdetsonly = browser.find_element_by_xpath().click()
cdetsonly = browser.find_element_by_xpath().click()


with open('query.txt') as f:
    queries = f.read().splitlines()

results_df = pd.DataFrame( columns=[])

for test in queries:
    lastupdate = []
    resolvedon = []
    if test == queries[]:
        search_box = browser.find_element_by_id().send_keys()
        search_box = browser.find_element_by_id().click()
        sleep(5)
        elem_search_box = browser.find_element_by_id()
        elem_search_box.clear()
        sleep(1)
        queries_xpath =
        lastupdate = browser.find_element_by_xpath().get_attribute("textContent")
        print()
        sleep(1)
        resolvequeries_xpath =
        resolvedon = browser.find_element_by_xpath().get_attribute("textContent")
        print()
        sleep(1)
        results_df_add = pd.Series([], index=results_df.columns)
        results_df = results_df.append(results_df_add,ignore_index=True)    
    else:
        search_box = browser.find_element_by_id().send_keys()
        search_box = browser.find_element_by_id().click()
        sleep(5)
        elem_search_box = browser.find_element_by_id()
        elem_search_box.clear()
        test_xpath =
        lastupdate = browser.find_element_by_xpath().get_attribute()
        print()
        sleep(1)
        resolveddts_xpath =
        resolvedon = browser.find_element_by_xpath().get_attribute("textContent")
        print()
        sleep(1)
        results_df_add = pd.Series([],index=results_df.columns)
        results_df = results_df.append(results_df_add,ignore_index=True)

        sleep(3)

results_df.to_csv("researchQuery.csv",index=False, mode='a', encoding="utf-8",)

#webdriver終了
browser.close()
browser.quit()

#ファイル閉じる
f.close()



