from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException, StaleElementReferenceException

from chatterbotapi import ChatterBotFactory, ChatterBotType
import time


factory = ChatterBotFactory()
#bot = factory.create(ChatterBotType.CLEVERBOT)
bot = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
botsession = bot.create_session()


def checkForStart( browser ):
	try:
		message = ""
		while(message != "You're now chatting with a random stranger. Say hi!"):
			message = browser.find_element_by_css_selector('.statuslog')
			message = message.get_attribute('innerHTML')
		return
	except StaleElementReferenceException:
		checkForStart( browser )


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

	checkForStart( browser )
	last_message = ""
	still_convo = True

	botsession = bot.create_session()
	question = browser.find_element_by_css_selector('.questionText').get_attribute('innerHTML')
	mymessage = botsession.think(question) 
	print " - - -- - - - - -- - - - - - - - - - -- - -  -- "
	print "Question: " + question; print

	try:
		chatbox = browser.find_element_by_css_selector('.chatmsg ')
		chatbox.send_keys(mymessage.lower())	
		time.sleep(len(mymessage.split()) * .5) # 70 WPM LOL
		chatbox.send_keys(Keys.RETURN)
		print "Trollbot> " + mymessage
	except InvalidElementStateException:
		True

	while(still_convo):	

		messages = browser.find_elements_by_css_selector('.strangermsg span')
		if(len(messages) > 0):
			message = messages[len(messages)-1].get_attribute('innerHTML')
			if(message != last_message):
				time.sleep(len(message.split()) * .5)
				last_message = message 
				mymessage = botsession.think(message) 				
				print "Stanger > " + last_message
				print "Trollbot> " + mymessage
				try:
					if(mymessage.endswith('.')):
						mymessage = mymessage[:len(mymessage)-1]
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
					discobutton = browser.find_element_by_css_selector('.disconnectbtn')
					discobutton.send_keys(Keys.ENTER)	
					still_convo = False		
					break; 
			except StaleElementReferenceException:
				True




