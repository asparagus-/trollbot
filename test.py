from chatterbotapi import ChatterBotFactory, ChatterBotType

"""
    chatterbotapi
    Copyright (C) 2011 pierredavidbelanger@gmail.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.
    
    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

factory = ChatterBotFactory()

bot = factory.create(ChatterBotType.CLEVERBOT)
botsession = bot.create_session()

print "--------------------------------------------------"

while (1):    
    message = raw_input("you> ")     
    message = botsession.think(message)
    print "bot> " + message


# # # # # # # # # # # # # ## errors ## # # # # # # # # # # # 
# urllib2.URLError: <urlopen error [Errno -2] Name or service not known>