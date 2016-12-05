from selenium import webdriver
import xlwt

driver = webdriver.Chrome()
driver.get("https://www.nur.kz/")

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Nur', cell_overwrite_ok = True)

cnt_coms = [cnt.text for cnt in driver.find_elements_by_xpath('//div[@class="news news-list__item"]/p[@class="news-list__comments"]')]
links = [a.get_attribute('href') for a in driver.find_elements_by_xpath('//div[@class="news news-list__item"]/a')]

for j in range(0, 1):
    if j==0:
        worksheet.write(0, j, "Title")
    
cnt=1	

for i in range(len(cnt_coms)):
    if cnt_coms[i] != '0':                                                                                                         
        driver.get(links[i])  
        comms  = driver.find_elements_by_xpath('//li[@class="answer__item"]')
        
        titles = driver.find_element_by_xpath('//div[@class="r"]//h1').text
        worksheet.write(i + len(comms) + 1, 0, titles)
        for comm in comms:     
            for k in range(1, 2):     #/html/body/section[2]/div[2]/section/div[3]/article/div[1]     
                if k==1:
                    texts = comm.find_element_by_xpath('.//html/body/section[2]/div[2]/section/div[3]/article/div[1]').text
                    worksheet.write(cnt, k, texts)   
              
                    worksheet.write(cnt, cnt)		
            cnt=cnt+1
workbook.save('final.xls')
