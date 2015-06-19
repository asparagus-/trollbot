from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException, StaleElementReferenceException

from chatterbotapi import ChatterBotFactory, ChatterBotType
import time


factory = ChatterBotFactory()
bot = factory.create(ChatterBotType.CLEVERBOT)
botsession = bot.create_session()


def checkForStart( browser ):
	message = ""
	while(message != "You're now chatting with a random stranger. Say hi!"):
		message = browser.find_element_by_css_selector('.statuslog')
		message = message.get_attribute('innerHTML')
	return



browser = webdriver.Firefox();
browser.get('https://www.omegle.com');

spymodebtn = browser.find_element_by_id('spymodebtn')
spymodebtn.send_keys(Keys.ENTER)

time.sleep(2)

startbutton = browser.find_element_by_css_selector("#tryspymodetext button")
buttonval = startbutton.get_attribute('innerHTML')
if(buttonval != 'Check it out!'):
	startbutton = browser.find_element_by_css_selector("#tryspymodetext a")
startbutton.send_keys(Keys.ENTER)

time.sleep(2)




while(True):
	still_convo = True
	checkForStart( browser )
	last_message = ""

	botsession = bot.create_session()
	question = browser.find_element_by_css_selector('.questionText').get_attribute('innerHTML')
	mymessage = botsession.think(question) 
	
	print "Question: " + question

	try:
		chatbox = browser.find_element_by_css_selector('.chatmsg ')
		chatbox.send_keys(mymessage.lower())	
		time.sleep(1)
		chatbox.send_keys(Keys.RETURN)
	except InvalidElementStateException:
		True

	while(True):
		time.sleep(2)

		messages = browser.find_elements_by_css_selector('.strangermsg span')
		if(len(messages) > 0):
			message = messages[len(messages)-1].get_attribute('innerHTML')
			if(message != last_message):
				last_message = message 
				mymessage = botsession.think(message) 				
				print "you> " + last_message
				print "bot> " + mymessage
				try:
					chatbox = browser.find_element_by_css_selector('.chatmsg ')
					chatbox.send_keys(mymessage.lower())
					time.sleep(len(mymessage.split()) * .7) # 70 WPM LOL
					chatbox.send_keys(Keys.RETURN)
				except InvalidElementStateException:
					True
				

		log = browser.find_elements_by_css_selector('.statuslog')
		for l in log:
			try:
				log_m = l.get_attribute('innerHTML')
				if ( log_m == 'Stranger has disconnected.'):	
					print "Stranger has disconnected."	
					print " - - -- - - - - -- - - - - - - - - - -- - -  -- "
					discobutton = browser.find_element_by_css_selector('.disconnectbtn')
					discobutton.send_keys(Keys.ENTER)			
					break
			except StaleElementReferenceException:
				True





