from googletrans import Translator
from pyrogram import Client, filters
from plugins.list import list
from database.gtrans_mdb import find_one, insert 
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["translate"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/translate")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"**Translated From {fromt.capitalize()} To {to.capitalize()}\n\n<code>{translation.text}</code>\n\nJoin [Star Movies Tamil](https://t.me/Star_Moviess_Tamil)**", disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))
			except:
			   	await message.reply_text(f"**Translated From {translation.src} To {translation.dest}\n\n<code>{translation.text}</code>\n\nJoin [Star Movies Tamil](https://t.me/Star_Moviess_Tamil)**", disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))
      			
				
			
		except :
			print("error")
	else:
			 ms = await message.reply_text("**You Can Use This Command with Your Language by using Reply to Message. You Can Get More Languages/list\n\n Example :-** <code>/translate Tamil</code>",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))

@Client.on_message(filters.private & filters.command(['list']))
async def list(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"<b>List is in The Form\nLanguage Code -> Language\n\nta -> தமிழ் -> Tamil\naf -> Afrikaans\nsq -> Albanian\nam -> Amharic\nar -> Arabic\nhy -> Armenian\naz -> Azerbaijani\neu -> Basque\nbe -> Belarusian\nbn -> Bengali\nbs -> Bosnian\nbg -> Bulgarian\nca -> Catalan\nceb -> Cebuano\nny -> Chichewa\nzh-cn -> Chinese\nco -> Corsican\nhr -> Croatian\ncs -> Czech\nda -> Danish\nnl -> Dutch\nen -> English\neo -> Esperanto\net -> Estonian\ntl -> Filipino\nfi -> Finnish\nfr -> French\nfy -> Frisian\ngl -> Galician\nka -> Georgian\nde -> German\nel -> Greek\ngu -> Gujarati\nht -> Haitian creole\nha -> Hausa\nhaw -> Hawaiian\niw -> Hebrew\nhi -> Hindi\nhmn -> Hmong\nhu -> Hungarian\nis -> Icelandic\nig -> Igbo\nid -> Indonesian\nga -> Irish\nit -> Italian\nja -> Japanese\njw -> Javanese\nkn -> Kannada\nkk -> Kazakh\nkm -> Khmer\nrw -> Kinyarwanda\nko -> Korean\nku -> Kurdish (kurmanji)\nky -> Kyrgyz\nlo -> Lao\nla -> Latin\nlv -> Latvian\nlt -> Lithuanian\nlb -> Luxembourgish\nmk -> Macedonian\nmg -> Malagasy\nms -> Malay\nml -> Malayalam\nmt -> Maltese\nmi -> Maori\nmr -> Marathi\nmn -> Mongolian\nmy -> Myanmar (burmese)\nne -> Nepali\nno -> Norwegian\nor -> Oriya\nps -> Pashto\nfa -> Persian\npl -> Polish\npt -> Portuguese\npa -> Punjabi\nro -> Romanian\nru -> Russian\nsm -> Samoan\ngd -> Scots gaelic\nsr -> Serbian\nst -> Sesotho\nsn -> Shona\nsd -> Sindhi\nsi -> Sinhala\nsk -> Slovak\nsl -> Slovenian\nso -> Somali\nes -> Spanish\nsu -> Sundanese\nsw -> Swahili\nsv -> Swedish\ntg -> Tajik\nta -> Tamil\ntt -> Tatar\nte -> Telugu\nth -> Thai\ntr -> Turkish\ntk -> Turkmen\nug -> Uighur\nuk -> Ukrainian\nur -> Urdu\nuz -> Uzbek\nvi -> Vietnamese\ncy -> Welsh\nxh -> Xhosa\nyi -> Yiddish\nyo -> Yoruba\nzu -> Zulu</b>",reply_to_message_id = message.id , parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )
			
