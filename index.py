from bs4 import BeautifulSoup
import requests
from google_images_download import google_images_download   #importing the library
import sys, os, re, subprocess, time, logging, math, wikipedia
from datetime import datetime, timedelta
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

from random import randint
from googletrans import Translator
from telethon.tl.custom import Button
import re
import urbandict
import json
trans = Translator()
import asyncio
from iso639 import languages
global ISAFK
global isSleeping
isSleeping = False
ISAFK = False
from rivescript import RiveScript

rs = RiveScript()
rs.load_file("./afk.ai")
rs.sort_replies()

global USERS
global reason
USERS={}
global COUNT_MSG
COUNT_MSG=0

import antispam
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest
from telethon.events import StopPropagation
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.functions.channels import LeaveChannelRequest, ExportInviteRequest, CreateChannelRequest

# Welcome to blank X's userbot file.
# Don't try to find for any personal information.
# Below, you'll see the api_id and api_hash. You will need to fill them in
# Almost all commands have /matrix, you can find /Usman and replace with whatever you like.

# Get your own at https://my.telegram.org
api_id = 192405
api_hash = '24e6f5fb10964323bef8e459828e4bcc'

from telethon.tl.functions.messages import AddChatUserRequest
# If you want to, you may enter the "scary"/uncommented cave/code below.
# It's dangerous though! You have been warned.

# client = TelegramClient('xen_', api_id, api_hash)
client = TelegramClient('blank', api_id, api_hash)

#

@client.on(events.NewMessage(outgoing=True, pattern='^.whois (.*)'))
async def whois(e):
	s = e.pattern_match.group(1)
	en = await client.get_entity(s)
	await e.reply(str(en))

@client.on(events.NewMessage(outgoing=True, pattern='^.tagall'))
async def whois(e):
	st = " "
	users = await client.get_participants(await client.get_input_entity(e.chat_id))
	for user in users:
		st = st + ("["+str(user.first_name)+"](tg://user?id="+str(user.id)+")\n")
	await e.reply(st)

@client.on(events.NewMessage(outgoing=True, pattern='^.pycmd (.*)'))
async def run(e):
	n=len(e.pattern_match.group(1))
	code = e.raw_text[n:]


	exec(
		f'async def __ex(e): ' +
		''.join(f'\n {l}' for l in code.split('\n'))
	)

	result = await locals()['__ex'](e)



@client.on(events.NewMessage(outgoing=True, pattern='^.wiki (.*)'))
async def wiki(e):
	await e.edit("Processing...")
	str = ''
	try:
		str = wikipedia.summary(e.pattern_match.group(1))
	except:
		await e.edit("Not found")
		return
	await e.edit(str)

# @client.on(events.NewMessage(outgoing=True, pattern='^.add'))
# async def wiki(e):
# 	participants = await client.get_participants(await client.get_input_entity(e.chat_id))
# 	users = ' '
# 	for user in participants:
# 		try:
# 			await client(AddChatUserRequest(
# 		    	400674061,
# 			    user.id,
# 			    fwd_limit=10
# 			))
# 		except:
# 			print("err")
		# print(user.id)
#trans
global tr
global translate_to
global translate_group
translate_group = []

tr = False
@client.on(events.NewMessage(pattern="^start translation (.+)"))
async def starttr(e):
	global tr
	global translate_to
	global translate_group
	tr = True
	translate_to = e.pattern_match.group(1)

	global translate_group
	translate_group.append(e.chat_id)

	await e.reply("Started translation to "+translate_to)

@client.on(events.NewMessage(pattern="^stop translation (.+)"))
async def starttr(e):
	global tr
	tr = False
	translate_group.remove(e.chat_id)
	await e.reply("Stopped translation")	

# auto translation


@client.on(events.NewMessage(outgoing=True))
async def f(e):
	global tr
	global translate_to
	global translate_group
	print (e.chat_id in translate_group)
	if tr:
		if e.chat_id in translate_group:
			to = translate_to
			await e.edit(trans.translate(e.raw_text, dest=to).text)

@client.on(events.NewMessage(pattern="marq (.+)"))
async def ls(e):
	x = e.pattern_match.group(1)
	for i in x:
		await e.edit(i)
		time.sleep(0.7)
@client.on(events.NewMessage(pattern="ls"))
async def ls(e):
	x = '😀😃😄😁😅😆😂🤣'
	for i in x:
		await e.edit(i)
		time.sleep(0.7)

@client.on(events.NewMessage(pattern="sl"))
async def ls(e):
	x = '😡😠😤😖😣☹️🙁😕🙂😊☺️'
	for i in x:
		await e.edit(i)
		time.sleep(0.7)



@client.on(events.NewMessage(pattern=".tran (.*)"))
async def tr(e):
        s = e.pattern_match.group(1)
        if e.is_reply: 
        	s = await e.get_reply_message()
        	s = s.message
        	if e.pattern_match.group(1):
        		to = e.pattern_match.group(1)
        	else:
        		to = 'en'
        	text = trans.translate(s, dest=to)
        	frm = languages.get(part1=text.src).name
        	await e.reply('From: '+frm+'\n'+text.text)
        	return
        to = re.findall(r"to=\w+", s)
        try:
        	to = to[0]
        	to = to.replace('to=', '')
        	s = s.replace('to='+to+' ', '')
        	print(s)
        	print('to='+to)
        except IndexError:
        	to = 'en'
        try:
        	text = trans.translate(s, dest=to)
        except:
        	await e.edit("Maybe wrong code name")
        	return
        frm = languages.get(part1=text.src).name
        await e.reply('From: '+frm+'\n'+text.text)


@client.on(events.NewMessage(outgoing=True, pattern=".img (.*)"))
async def img(e):
	await e.edit('Processing...')
	start=round(time.time() * 1000)
	s = e.pattern_match.group(1)
	lim = re.findall(r"lim=\d+", s)
	try:
		lim = lim[0]
		lim = lim.replace('lim=', '')
		s = s.replace('lim='+lim[0], '')
	except IndexError:
		lim = 2
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":s,"limit":lim, "format":"jpg"}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	lst = paths[s]
	await client.send_file(await client.get_input_entity(e.chat_id), lst)
	end=round(time.time() * 1000)
	msstartend=int(end) - int(start)
	await e.edit("Done. Time taken: "+str(msstartend) + 's')


#ud
@client.on(events.NewMessage(pattern='^.ud (.*)'))
async def ud(e):
	await e.edit("Processing...")
	str = e.pattern_match.group(1)
	try:
		mean = urbandict.define(str)
	except:
		await e.edit("Not found.")
		return
	if len(mean) >= 0:
		await e.edit('Text: **'+str+'**\n\nMeaning: **'+mean[0]['def']+'**\n\n'+'Example: \n__'+mean[0]['example']+'__')
	else:
		await e.edit("No result found for **"+str+"**")

#what is
page = requests.get('http://google.com/search?q=define+api')
soup = BeautifulSoup(page.text, 'html.parser')
print (soup.find(class_='PNlCoe XpoqFe'))
# html = open('test.html', 'w')
# html.write(str(soup))

@client.on(events.NewMessage(pattern='^.whatis (.*)'))
async def whatis(e):
	s = e.pattern_match.group(1)
	page = requests.get('http://google.com/search?q='+s)
	soup = BeautifulSoup(page.text, 'html.parser')
	print(soup.find(class_='mrH1y'))

# @client.on(events.ChatAction(chats=[-1001178537590, -1001215689666]))
# async def proxydel(e):
# 	if e.user_added == True:
# 		await e.delete()
# 	elif e.user_joined == True:
# 		await e.delete()
# 	elif e.user_left == True:
# 		await e.delete()
# 	elif e.user_kicked == True:
# 		await e.delete()


@client.on(events.NewMessage(pattern=r'^.google (.*)'))
async def gsearch(e):
	match = e.pattern_match.group(1)
	result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
	result=str(result_.stdout.decode())
	await client.send_message(await client.get_input_entity(e.chat_id), message='**Search:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)

@client.on(events.NewMessage(outgoing=True, pattern=r'^.eval (.*)'))
async def gsearch(e):
	s = e.pattern_match.group(1)
	await e.reply(str(eval(s)))


# spam
@client.on(events.NewMessage(outgoing=True, pattern='.spam'))
async def spammer(event):
    message=await client.get_messages(event.chat_id)
    counter=int(message[0].message[6:8])
    spam_message=str(event.text[8:])
    await asyncio.wait([event.respond(spam_message) for i in range(counter)])
    await event.delete()



@client.on(events.NewMessage(outgoing=True))
async def ownerpowers(e):
	if '.upload ' in e.raw_text:
		await e.reply(e.raw_text[14:], file=e.raw_text[14:])
	elif '.restart' == e.raw_text:
		await e.reply('`Yes, my master, I will restart now.`')
		os.execl(sys.executable, sys.executable, *sys.argv)
	elif '.cmd ' in e.raw_text:
		cmd=e.raw_text[4:]
		cmd = cmd.split(" ")
		# output = subprocess.check_output(cmd, shell=True)
		# print(output)
		cmd0=subprocess.check_output(cmd, stdout=subprocess.PIPE)
		# cmd1=str(output.stdout.decode())
		if len(output) > 4096:
			await e.reply('`My master, I am sorry but I cannot do it. It\'s too big.`')
		else:
			await e.reply('`' + cmd1 + '`')

	elif '.block' == e.raw_text:
		if '-' not in str(e.chat_id):
			await client(BlockRequest(await client.get_input_entity(e.chat_id)))
	elif '.leave' == e.raw_text:
		if '-' in str(e.chat_id):
			await client(LeaveChannelRequest(e.chat_id))

@client.on(events.NewMessage)
async def my_e_handler(e):
	if '.matrix ping' == e.raw_text:
		start=round(time.time() * 1000)
		pongmsg=await e.reply('Pong!')
		end=round(time.time() * 1000)
		msstartend=int(end) - int(start)
		await client(EditMessageRequest(peer=e.chat_id, id=pongmsg.id, message='Pong!\n' + str(msstartend) + 'ms'))
	elif '.msgid' == e.raw_text:
		await e.reply('There are ' + str(e.id + 1) + ' messages (including this one) in this chat')
	elif '.random' == e.raw_text:
		rannum = randint(0, 69420)
		await e.reply(str(rannum))
	elif '.antispam' in e.raw_text:
		checkspam=str(e.raw_text[11:])
		spamscore=str(antispam.score(checkspam))
		spambool=str(antispam.is_spam(checkspam))
		await e.reply('Spam results for `' + checkspam + '`\nScore: ' + spamscore + '\nIs Spam: ' + spambool)

global antispamStat
antispamStat = False

@client.on(events.NewMessage(outgoing=True, pattern='^.as on'))
async def changeas(event):
	await event.edit("Antispam is now on")
	global antispamStat
	antispamStat = True

@client.on(events.NewMessage(outgoing=True, pattern='^.as off'))
async def changeasoff(event):
	await event.edit("Antispam is now off")
	global antispamStat
	antispamStat = False


@client.on(events.NewMessage(incoming=True))
async def mention_afk(event):
    global COUNT_MSG
    global USERS
    global ISAFK
    global antispamStat
    #if antispam.is_spam(event.raw_text) and antispamStat:
    	#await event.reply("Please dont spam")
    if event.message.mentioned:
        if ISAFK:
            if event.chat_id not in USERS:
                  await event.reply("Sorry! Master Usman is currently away from keyboard")
                  USERS.update({event.chat_id:1})
                  COUNT_MSG=COUNT_MSG+1
            elif event.chat_id in USERS:
                 if USERS[event.chat_id] % 5 == 0:
                      await event.reply("Sorry! But Master Usman is still not here. Try to ping him later. I am sorry😖")
                      USERS[event.chat_id]=USERS[event.chat_id]+1
                      COUNT_MSG=COUNT_MSG+1
                 else:
                   USERS[event.chat_id]=USERS[event.chat_id]+1
                   COUNT_MSG=COUNT_MSG+1

@client.on(events.NewMessage(outgoing=True, pattern='^.afk'))
async def afk(e):
	await e.edit('I am Away From Keyboard.')
	global ISAFK
	ISAFK=True

@client.on(events.NewMessage(outgoing=True, pattern='^.back'))
async def not_afk(event):
            global ISAFK
            global COUNT_MSG
            global USERS
            ISAFK=False
            await event.edit("Hi Guys! I am back!")
            await event.respond("You had recieved "+str(COUNT_MSG)+" messages while you were away")
            COUNT_MSG=0
            USERS={}
#purgme
@client.on(events.NewMessage(outgoing=True, pattern='.pme'))
async def purgeme(event):
    message=await client.get_messages(event.chat_id)
    count = int(message[0].message[4:])
    i=1
    async for message in client.iter_messages(event.chat_id,from_user='me'):
        if i>count+1:
            break
        i=i+1
        await message.delete()
#-_-
@client.on(events.NewMessage(outgoing=True, pattern='uhm'))
async def face(event):
	s = '_'
	for i in range(10):
		await event.edit('-'+s+'-')
		s+='_'
		time.sleep(0.4)

@client.on(events.NewMessage(outgoing=True, pattern='meh'))
async def face(event):
	for i in range(10):
		if i % 2 == 0:
			await event.edit(':/')
		else:
			await event.edit(':\\')
		time.sleep(0.8)


client.start()
logging.basicConfig(level=logging.ERROR)
client.run_until_disconnected()
