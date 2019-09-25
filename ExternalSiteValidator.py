def data_Check(driver):
	try:
		from CSV_Function import csvRead, csvWrite, csvAppend
		import datetime
		import csv
		import os
		import time
		from check_xpath_exists import check_exists_by_xpath
		import glob
		# get bot id from function
		from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
		from random import randint
		time.sleep(randint(1,10))

		# create csv for bot_start
		timeStamp = [[str(datetime.datetime.now().microsecond)]]
		bot_ids = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\Multi_threading_active_bots\\bot_*.csv'
		bot_id = len(glob.glob(bot_ids))
		csvPre = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\Multi_threading_active_bots\\bot_'
		csvSuf = '.csv'
		
		csvPath = csvPre + 'start_' + str(bot_id) + csvSuf

		u_a = csvRead(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\user_agents_new.csv")
		
		

		

		with open(csvPath, 'w', newline='') as writeFile:
			writer = csv.writer(writeFile, lineterminator='\n')
			writer.writerows(timeStamp)	
	 
		# load in csvFiles

		with open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\My_scripts\SEO_Scraping\DomainAgents\domain_agents_csv.csv",newline='') as ff:
			data = list(csv.reader(ff))

		# check if temp file exists
		i = 0


		tempPre = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\My_scripts\\SEO_Scraping\\DomainAgents\\CSV_temp\\temp_domain_agents_'
		

		RealPre = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\My_scripts\\SEO_Scraping\\DomainAgents\\CSV_Parts\\scappedURL_'

		URL_PRE = #URL USED TO CHECK DATA
		
		domainsNames = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\scraped\\domainNames'
		from Int_Check import Int_Check
		print(len(data[0]))
		
		if( i < len(data[0])):
			while (i < len(data[0])):
				#print("entered")

				tempFile = tempPre + str(i) + csvSuf
				# if no temp file, create temp file with timestamp
				
				if(os.path.isfile(tempFile) == False):
					
					timeStamp = [[str(datetime.datetime.now().microsecond)]]
					csvWrite(tempFile, [[bot_id]])

					
					# ensure record datetime variables match
					time.sleep(5)
					with open(tempFile,'r',newline='') as f:
						varCheck = list(csv.reader(f))
					#print(bot_id)
					#print(int(varCheck[0][0]))
					time.sleep(5)
					if(int(varCheck[0][0]) == bot_id):


						# get all domains in batch
						fileName = RealPre + str(i) + csvSuf
						with open(fileName, 'r',newline='') as fff:
							files = list(csv.reader(fff))

						if len(files) > 0:
							j = 0
							flag = False
								
							print(len(files))	
							if (j < len(files)):
								while(j < len(files)):
								
									if i >= 0:
										#print("entered")
										queryURL = URL_PRE + files[j][0]
										driver.delete_all_cookies()
										user_agent = ",".join(u_a[randint(0,len(u_a)-1)])
										driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":user_agent})#, "platform":"Windows"})		
										time.sleep(randint(1,4))
										driver.get(queryURL)							
										current_url = driver.current_url
										#print(current_url)
										url_checker = 'seoprofiler' in current_url
										CEO = False
										if(check_exists_by_xpath(driver,'//img[@alt="CEO"]') == True):
											CEO = driver.find_element_by_xpath('//img[@alt="CEO"]').is_displayed()
										
										#print('CEO is on screen ' + str(CEO))

										#print("Url checker is " + str(url_checker))
										if (CEO == True or url_checker == True):
											flag = True

										if flag == True:
											print("Flag Test entered")
											ii = 0
											while flag == True and ii < 1:
												driver.delete_all_cookies()
												time.sleep(randint(1,4))
												#user_agent = ",".join(u_a[randint(0,len(u_a)-1)])
												#driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":user_agent})#, "platform":"Windows"})

												driver.get(queryURL)
												current_url = driver.current_url
												url_checker = 'seoprofiler' in current_url
												if(check_exists_by_xpath(driver,'//img[@alt="CEO"]') == False):
													CEO = False
												print("Domain refreshed on CEO " + str(CEO) + " and on url_Checker " + str(url_checker) + " on count " + str(ii))
												print(queryURL)
												if (CEO == False and url_checker == False):
													flag = False

												ii = ii + 1	

												if ii == 1:
													driver.quit()
													time.sleep(1)
													from Bot_Threading_v2_restart import new_driver
													j = j + 1
													new_driver(fileName,i,j,bot_id)
													#break
													#break
													#break
													#exit()


										#print("flag is " + str(flag))
										
										LIS = 0
										if flag == False:		
											if(check_exists_by_xpath(driver, '//span[contains(text(),"Link Influence Score")]//..//span[@class="info-box-number"]') == True):
												LIS = driver.find_element_by_xpath('//span[contains(text(),"Link Influence Score")]//..//span[@class="info-box-number"]').text
											
												if(Int_Check(LIS[0:LIS.index('%')]) == True):
													LIS = int(LIS[0:LIS.index('%')])
												else:
													LIS = 0

												if(check_exists_by_xpath(driver, '//div[contains(text(),"Industry:")]') == True):

													industry = driver.find_element_by_xpath('//div[contains(text(),"Industry:")]').text
													industryIndex = industry.index('Industry:')+len('Industry')
													industry = industry[industryIndex:].strip()
												else:
													industry = 'unknown'



											
												if(LIS >= 30):
													print("LIS entered csv file")
													
													# create own csv file for good domains by bot_ID
													good_domains = [['Domain_Agents'],[files[j]],[LIS],[industry]]
													GoodDomainCSV = domainsNames + str(bot_id) + csvSuf
													print(GoodDomainCSV)
													dupeCheck = False
													if(os.path.isfile(GoodDomainCSV) == False):
														with open(GoodDomainCSV,'w',newline='') as fd:
															writer = csv.writer(fd, lineterminator='\n')
															writer.writerows(good_domains)	
														dupeCheck = True

													if(os.path.isfile(GoodDomainCSV) == True and dupeCheck == False):
														with open(GoodDomainCSV,'a',newline='') as fd:
															writer = csv.writer(fd, lineterminator='\n')
															writer.writerows(good_domains)	
											print("LIS on the page " + str(LIS))
									j = j + 1


				i = i  + 1
		
				# create csv for bot_end -- match with bot_start to run data wiping, csv consolidation to single report
				if( i == len(data[0])):
					driver.quit()
					csvPath2 = csvPre + 'end_' + str(bot_id) + csvSuf
					
					csvChecker1 = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\Multi_threading_active_bots\\bot_start*.csv'
					csvChecker2 = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\Multi_threading_active_bots\\bot_end*.csv'
					csvChecker1 = glob.glob(csvChecker1)
					csvChecker2 = glob.glob(csvChecker2)

					if(len(csvChecker1) == len(csvChecker2)+1):
						import emailer
		
	except Exception as e:
		#import sys
		#import datetime
		#from Error_email import Error_email
		#scriptname = sys.argv[0]
		#timestamp = datetime.datetime.now()
		#errorMsg = repr(e)
		#Error_email(scriptname,timestamp,errorMsg)
		driver.quit()
		exit()




