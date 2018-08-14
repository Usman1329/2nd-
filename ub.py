# Continue below, I'm just importing some things. (Line 7)

import sys, os, re, subprocess, time, logging, math
from datetime import datetime, timedelta
from random import randint

# Quick question! Do you have git installed?
# If no, change gitinstalled to False
gitinstalled = True
# Now continue to line 48

start=round(time.time() * 1000)

platforms = {
    'win32' : 'Windows'
    }
if sys.platform not in platforms:
    subprocess.run(['pip3', 'install', '-U', 'pip'], stdout=subprocess.PIPE)
else:
	subprocess.run(['python', '-m', 'pip3', 'install', '-U', 'pip'], stdout=subprocess.PIPE)
	
if gitinstalled == True:
	subprocess.run(['pip3', 'install', '-U', '--no-cache', 'git+https://github.com/LonamiWebs/Telethon@master'], stdout=subprocess.PIPE)
else:
	subprocess.run(['pip3', 'install', '-U', 'telethon'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'datetime'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'antispam'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'gsearch'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'hashtools'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'pybase64'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'pyHIBP'], stdout=subprocess.PIPE)
subprocess.run(['pip3', 'install', '-U', 'requests'], stdout=subprocess.PIPE)
if gitinstalled == True:
	subprocess.run(['git', 'clone', 'https://github.com/alvations/rubberduck'], stdout=subprocess.PIPE)
	
end=round(time.time() * 1000)
msstartend=int(end) - int(start)
secstartend=str(msstartend / 1000)

import antispam, pybase64, pyHIBP, requests
from pyHIBP import pwnedpasswords as pw
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest
from telethon.events import StopPropagation
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.functions.channels import LeaveChannelRequest, ExportInviteRequest, CreateChannelRequest

# Welcome to blank X's userbot file.
# Don't try to find for any personal information.
# Below, you'll see the api_id and api_hash. You will need to fill them in
# Almost all commands have /blank, you can find /blank and replace with whatever you like.

# Get your own at https://my.telegram.org
api_id = 694206
api_hash = 'insertanexamplevalueeditthese'
# This is your logging channel ID/username.
logc=-1001360011268
# If you don't want a logging channel, change enablelogc to False
enablelogc = True
# Do you want to change hi to H0I!!!, If no, change it to false
hi2hoi = True

# If you want to, you may enter the "scary"/uncommented cave/code below.
# It's dangerous though! You have been warned.

client = TelegramClient('blank', api_id, api_hash)
blankfloodcount = 0
isafk = False
afkreason = 'If you see this as an AFK reason, my developer (@blank_x) screwed up.'
onlyowner = False
onlyne = False

@client.on(events.NewMessage(chats=['@PublicTestGroup', '@SnowballFight', '@BotTalk']))
async def end(e):
	raise StopPropagation
	
@client.on(events.NewMessage(chats=['@TelethonUpdates']))
async def telethonupdate(e):
	global gitinstalled
	if gitinstalled == True:
		subprocess.run(['pip3', 'install', '-U', '--no-cache', 'git+https://github.com/LonamiWebs/Telethon@master'], stdout=subprocess.PIPE)
	else:
		subprocess.run(['pip3', 'install', '-U', 'telethon'], stdout=subprocess.PIPE)
	
@client.on(events.ChatAction(chats=[-1001178537590, -1001215689666]))
async def proxydel(e):
	if e.user_added == True:
		await e.delete()
	elif e.user_joined == True:
		await e.delete()
	elif e.user_left == True:
		await e.delete()
	elif e.user_kicked == True:
		await e.delete()
		
@client.on(events.NewMessage(incoming=True))
async def zero(e):
	global onlyowner
	if onlyowner == True:
		raise StopPropagation

@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank spam ([0-9]+) (.*)'))
async def spammmm(e):
	x=int(e.pattern_match.group(1))
	for x in range(int(e.pattern_match.group(1))):
		await e.respond(e.pattern_match.group(2))
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank log (.*)'))
async def logdis(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, 'Custom owner message: ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank owneronly (yes|no)$'))
async def ownerrrznly(e):
	global onlyowner
	if e.pattern_match.group(1) == 'yes':
		onlyowner = True
		await e.reply('`My master, now only you can use me.`')
	else:
		onlyowner = False
		await e.reply('`My master, now others and you can use me.`')
	
@client.on(events.NewMessage(pattern=r'^/blank unshorten (.*)'))
async def unshortenurl(e):
	session = requests.Session()
	resp=session.head(e.pattern_match.group(1), allow_redirects=True)
	await e.reply('Unshortened link: ' + resp.url)
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank owneronly yes$'))
async def blankfraudchkm1(e):
	global enablelogc
	if enablelogc == True:
		global logc
		if e.pattern_match.group(1) == 'yes':
			await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to enable owner only')
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank '))
async def blankfraudchk(e):
	global enablelogc
	if enablelogc == True:
		global logc
		if '/blank restart' == e.raw_text:
			await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to restart the userbot')
		elif '/blank block' == e.raw_text:
			if 0 < e.chat_id:
				await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to block themselves')
		elif '/blank leave' == e.raw_text:
			if 0 > e.chat_id:
				await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you leave ' + str(e.chat_id))
				
@client.on(events.NewMessage(outgoing=True, pattern=r'^(?i)hi$'))
async def hoi(e):
	global hi2hoi
	if hi2hoi == True:
		await e.edit('H0`I`!!!')
				
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank cmd (.*)'))
async def blankfraudchk0(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you execute ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank freeze ([0-9]+)'))
async def blankfraudchk1(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to freeze you for ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank spam ([0-9]+) (.*)'))
async def blankfraudchk2(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you spam `' + e.pattern_match.group(2) + '` ' + e.pattern_match.group(1) + ' times')
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank upload (.*)'))
async def blankfraudchk3(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you upload ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank afk (.*)'))
async def blankfraudchk4(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you AFK because ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(incoming=True, pattern=r'^(/blank pycmd ).*'))
async def blankfraudchk5(e):
	global enablelogc
	if enablelogc == True:
		global logc
		n=len(e.pattern_match.group(1))
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you execute (py)\n' + e.raw_text[n:])
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^(/blank pycmd ).*'))
async def run(e):
	n=len(e.pattern_match.group(1))
	code = e.raw_text[n:]
	# written by [Twit](t.me/youtwitface) and copied by [blank](t.me/blank_x) (piece of shit)

	exec(
		f'async def __ex(e): ' +
		''.join(f'\n {l}' for l in code.split('\n'))
	)

	result = await locals()['__ex'](e)

@client.on(events.NewMessage(pattern=r'^/blank ddg (.*)'))
async def ddg(e):
	global gitinstalled
	if gitinstalled == True:
		match = e.pattern_match.group(1)
		result_=subprocess.run(['python', 'rubberduck/rbd.py', '-m', match], stdout=subprocess.PIPE)
		result=str(result_.stdout.decode())
		url_=subprocess.run(['python', 'rubberduck/rbd.py', '-u', match], stdout=subprocess.PIPE)
		url=str(url_.stdout.decode())
		await client.send_message(await client.get_input_entity(e.chat_id), message='**Search:**\n`' + match + '`\n\n**Result:**\n`' + result + '`\n**URL:**\n' + url, reply_to=e.id, link_preview=False)
	else:
		await e.reply('`According to the settings my master has given me, I believe the files required aren\'t here.`')
	
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank figlet (.*)'))
async def figletzchk(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you figlet ' + e.pattern_match.group(1))

@client.on(events.NewMessage(pattern=r'^/blank google (.*)'))
async def gsearch(e):
	match = e.pattern_match.group(1)
	result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
	result=str(result_.stdout.decode())
	await client.send_message(await client.get_input_entity(e.chat_id), message='**Search:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)

@client.on(events.NewMessage(incoming=True, pattern=r'^(/blank|@kaeldas$|coolegg$|TEM$)'))
async def antiblankflood(e):
	global blankfloodcount
	global onlyowner
	blankfloodcount += 1
	if blankfloodcount >= 7:
		onlyowner = True
		global enablelogc
		if enablelogc == True:
			global logc
			await client.send_message(logc, 'Flood cout have been surpassed.')
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank upload (.*)'))
async def ownerupload(e):
	match = e.pattern_match.group(1)
	await e.reply(e.raw_text[14:], file=e.raw_text[14:])
	
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank cmd (.*)'))
async def ownercmd(e):
	cmd=e.pattern_match.group(1).split(' ')
	cmd0=subprocess.run(cmd, stdout=subprocess.PIPE)
	cmd1=str(cmd0.stdout.decode())
	if len(cmd1) > 4096:
		await e.reply('`My master, I am sorry but I cannot do it. It\'s too big.`')
	else:
		await e.reply('`' + cmd1 + '`')
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank freeze ([0-9]+)$'))
async def ownerfreeze(e):
	match = e.pattern_match.group(1)
	await e.reply('`I see, I will freeze myself for ' + match + ' seconds.`')
	time.sleep(int(match))
	
@client.on(events.NewMessage(incoming=True))
async def afkin(e):
	global isafk
	global afkreason
	if 0 < e.chat_id:
		if isafk == True:
			await e.reply('`Sir, my master has told me (my master\'s userbot) that he is AFK.\n\nReason: ' + afkreason + '`')
	elif '@blank_x' in e.raw_text:
		if isafk == True:
			await e.reply('`Sir, my master has told me (my master\'s userbot) that he is AFK.\n\nReason: ' + afkreason + '`')
	elif e.mentioned == True:
		if isafk == True:
			await e.reply('`Sir, my master has told me (my master\'s userbot) that he is AFK.\n\nReason: ' + afkreason + '`')
			
@client.on(events.NewMessage(outgoing=True))
async def afkout(e):
	global isafk
	if isafk == True:
		isafk = False
		await e.reply('`Sir, your AFK status is now off.`')
		
@client.on(events.NewMessage(outgoing=True))
async def ownerpowers(e):
	global isafk
	if '/blank restart' == e.raw_text:
		await e.reply('`Yes, my master, I will restart now.`')
		os.execl(sys.executable, sys.executable, *sys.argv)
	elif '/blank block' == e.raw_text:
		if '-' not in str(e.chat_id):
			await client(BlockRequest(await client.get_input_entity(e.chat_id)))
	elif '/blank leave' == e.raw_text:
		if '-' in str(e.chat_id):
			await client(LeaveChannelRequest(e.chat_id))
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank afk (.*)'))
async def afkout0(e):
	global afkreason
	afkreason = e.pattern_match.group(1)
	global isafk
	isafk = True
	await e.reply('`My master, your AFK status is on.`')
			
@client.on(events.NewMessage(pattern=r'^/blank antispam (.*)'))
async def antispam(e):
	checkspam=e.pattern_match.group(1)
	spamscore=str(antispam.score(checkspam))
	spambool=str(antispam.is_spam(checkspam))
	await e.reply('Spam results for `' + checkspam + '`\nScore: ' + spamscore + '\nIs Spam: ' + spambool)

@client.on(events.NewMessage(pattern=r'^/blank hash (.*)'))
async def hash(e):
	hashtxt_ = e.pattern_match.group(1)
	hashtxt=open('hashdis.txt','w+')
	hashtxt.write(hashtxt_)
	hashtxt.close()
	md5=subprocess.run(['md5', 'hashdis.txt'], stdout=subprocess.PIPE)
	md5=md5.stdout.decode()
	sha1=subprocess.run(['sha1', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha1=sha1.stdout.decode()
	sha256=subprocess.run(['sha256', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha256=sha256.stdout.decode()
	sha512=subprocess.run(['sha512', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha512=sha512.stdout.decode()
	ans='Text: `' + hashtxt_ + '`\nMD5: `' + md5 + '`SHA1: `' + sha1 + '`SHA256: `' + sha256 + '`SHA512: `' + sha512[:-1] + '`'
	if len(ans) > 4096:
		await e.reply('`Sir, I can\'t send the hashes.`')
	else:
		await e.reply(ans)
		
@client.on(events.NewMessage(pattern=r'^/blank base64 (en|de)code (.*)'))
async def endecrypt(e):
	if e.pattern_match.group(1) == 'en':
		lething=str(pybase64.b64encode(bytes(e.pattern_match.group(2), 'utf-8')))[2:]
		await e.reply('Encoded: `' + lething[:-1] + '`')
	else:
		lething=str(pybase64.b64decode(bytes(e.pattern_match.group(2), 'utf-8'), validate=True))[2:]
		await e.reply('Decoded: `' + lething[:-1] + '`')
		
@client.on(events.NewMessage(outgoing=True, pattern=r'^/blank nomarkdown (.*)'))
async def nomarkdown(e):
	await client(EditMessageRequest(peer=e.chat_id, id=e.id, message=e.pattern_match.group(1)))
	
@client.on(events.NewMessage(incoming=True, pattern=r'^/blank nomarkdown (.*)'))
async def nomarkdownchk(e):
	global enablelogc
	if enablelogc == True:
		global logc
		await client.send_message(logc, '[' + str(e.from_id) + '](tg://user?id=' + str(e.from_id) + ') tried to make you no markdown ' + e.pattern_match.group(1))
		
@client.on(events.NewMessage(pattern=r'^/blank pwned (.*)'))
async def pwned(e):
	lething=await e.reply('`Searching . . .`')
	resp=pw.is_password_breached(password=e.pattern_match.group(1))
	if resp:
		if resp > 1:
			await lething.edit('`Password is breached ' + str(resp) + ' times.`')
		else:
			await lething.edit('`Password is breached 1 time.`')
	else:
		await lething.edit('`Password isn\'t breached, you\'re save.`')
	
@client.on(events.NewMessage)
async def my_e_handler(e):
	if '/blank ping' == e.raw_text:
		start=round(time.time() * 1000)
		pongmsg=await e.reply('Pong!')
		end=round(time.time() * 1000)
		msstartend=int(end) - int(start)
		await client(EditMessageRequest(peer=e.chat_id, id=pongmsg.id, message='Pong!\n' + str(msstartend) + 'ms'))
	elif '/blank msgid' == e.raw_text:
		await e.reply('The message id is ' + str(e.id + 1) + ' (includes this)')
	elif '/blank random' == e.raw_text:
		rannum = randint(0, 69420)
		await e.reply(str(rannum))
	elif '/blank killme' == e.raw_text:
		name = await client.get_entity(e.from_id)
		name0 = str(name.first_name)
		await e.reply('**K I L L  **[' + name0 + '](tg://user?id=' + str(e.from_id) + ')**\n\nP L E A S E\n\nE N D  T H E I R  S U F F E R I N G**')
	elif '/blank' == e.raw_text:
		if '-' not in str(e.chat_id):
			await client.send_message(await client.get_input_entity(e.chat_id), message='[Read the f---ing channel](t.me/blank_x_userbot) (jk u dont have 2)', reply_to=e.id, link_preview=False)
		else:
			await e.reply('`Sir, to avoid some stuff, do it in pm.`')
	elif '@kaeldas' in e.raw_text:
		await e.reply('**H E  I S  D E A D**')
	elif 'TEM' == e.raw_text:
		await e.reply('h0`I`!!!!!! i\'m tEMMIE!!\n\nuS tEms haV veRY dEP HisTOrY!')
	elif 'coolegg' == e.raw_text:
		await e.reply('TEM want 2 pursue higher education')
	elif 'Created a new game! Join the game with /join and start the game with /start' == e.raw_text:
		if 592767512 == e.from_id:
			if -1001371304731 == e.chat_id:
				await e.reply('/join by userbot\n@ceda_ei wanna join?\nIf this is an error, then tell me this is an error.')
			elif -1001390088897 == e.chat_id:
				await e.reply('/join by userbot\n@ceda_ei wanna join?\nIf this is an error, then tell me this is an error.')
	elif 'Closed the lobby. No more players can join this game.' == e.raw_text:
		if 592767512 == e.from_id:
			await e.reply('/open@puno_bot by userbot\nif this is an error then tell me this is an error.')

@client.on(events.NewMessage(chats=(-1001178537590), pattern=r'^!ot$'))
async def ot(e):
	await client.delete_messages(e.input_chat, [e.id])
	await client.send_message(await client.get_input_entity(e.chat_id), message='Please go to the [Off-topic group](t.me/proxytalkofftopic)', reply_to=e.reply_to_msg_id, link_preview=False)

@client.on(events.NewMessage)
async def usboton(e):
	global onlyne
	global enablelogc
	if enablelogc == True:
		if onlyne == False:
			global logc
			global secstartend
			onlyne = True
			await client.send_message(logc, 'Userbot is now online, took me ' + secstartend + ' seconds')
	
client.start()
logging.basicConfig(level=logging.ERROR)
client.run_until_disconnected()