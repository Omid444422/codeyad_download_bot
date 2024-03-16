from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from time import sleep
from json import dumps

print('enter username:')
username = str(input(': '))

print('enter password:')
password = str(getpass(': '))

print('enter course_url:')
course_url = str(input(': '))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://codeyad.com')

course_data = list()

sleep(5)

close_ad_button = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/div/div[2]/div/div/button')
close_ad_button.click()

btn_login = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/header/div/section[1]/div[2]/button')
btn_login.click()

sleep(1)

email_input = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/div/div[2]/div/div/form/div[1]/div/input')
email_input.send_keys(username)

password_input = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/div/div[2]/div/div/form/div[2]/div/input')
password_input.send_keys(password)

submit_login_btn = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/div/div[2]/div/div/form/button[2]')
submit_login_btn.click()

sleep(1)


driver.get(course_url)

sleep(5)

course_name = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/main/div/aside/h1').text

course_seasons = driver.find_elements(By.CSS_SELECTOR,'div.head.items-center')

for single_season in course_seasons:
        season_data = {'name':None,'urls':list()}

        driver.execute_script("arguments[0].scrollIntoView();", single_season)
        sleep(2)

        single_season.click()

        sleep(2)


        season_name = single_season.find_element(By.XPATH,'.//p').text

        season_data['name'] = season_name
        course_data.append(season_data)

season_content = driver.find_elements(By.CSS_SELECTOR,'div.content.mt-2')

for counter,content in enumerate(season_content):

    driver.execute_script("arguments[0].scrollIntoView();", content)

    sleep(2)

    episodes = content.find_elements(By.XPATH,'.//div[@class="flex gap-2 items-center justify-between"]')

    for episode in episodes:
        episode_data = {'name':None,'url':None}

        episode.click()

        sleep(2)

        try:
          watched_div = driver.find_element(By.XPATH,'//*[@id="player"]/div/button[@class="btn relative !text-white bg-green hover:!bg-green-950"]')
          watched_div.click()

        except:
          pass   
        
        sleep(2)

        driver.execute_script("arguments[0].scrollIntoView();", episode)

        sleep(2)

        episode_name = episode.find_element(By.XPATH,'.//a/p').text
            
        episode_download_button = episode.find_element(By.XPATH,'.//button[1]')
        episode_download_button.click()

        sleep(2)

        driver.switch_to.window(driver.window_handles[1])
            
        episode_url = driver.current_url

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        episode_data['name'] = episode_name
        episode_data['url'] = episode_url
        course_data[counter]['urls'].append(episode_data)

        print(episode_data)

        sleep(2)



print('*' * 150)
print(course_data)

course_data_json = dumps(course_data,ensure_ascii=False)

with open(f'{course_name}.json','w',encoding='utf-8') as course_json_file:
     course_json_file.write(course_data_json)

print('ended successfull')

driver.close()