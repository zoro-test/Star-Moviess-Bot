from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from database.gtrans_mdb import set, unset, insert
from plugins.list import list

@Client.on_message(filters.private & filters.command(['list']))
async def list(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"<b>List is in The Form\nLanguage Code -> Language\n\nta -> தமிழ் -> Tamil\naf -> Afrikaans\nsq -> Albanian\nam -> Amharic\nar -> Arabic\nhy -> Armenian\naz -> Azerbaijani\neu -> Basque\nbe -> Belarusian\nbn -> Bengali\nbs -> Bosnian\nbg -> Bulgarian\nca -> Catalan\nceb -> Cebuano\nny -> Chichewa\nzh-cn -> Chinese\nco -> Corsican\nhr -> Croatian\ncs -> Czech\nda -> Danish\nnl -> Dutch\nen -> English\neo -> Esperanto\net -> Estonian\ntl -> Filipino\nfi -> Finnish\nfr -> French\nfy -> Frisian\ngl -> Galician\nka -> Georgian\nde -> German\nel -> Greek\ngu -> Gujarati\nht -> Haitian creole\nha -> Hausa\nhaw -> Hawaiian\niw -> Hebrew\nhi -> Hindi\nhmn -> Hmong\nhu -> Hungarian\nis -> Icelandic\nig -> Igbo\nid -> Indonesian\nga -> Irish\nit -> Italian\nja -> Japanese\njw -> Javanese\nkn -> Kannada\nkk -> Kazakh\nkm -> Khmer\nrw -> Kinyarwanda\nko -> Korean\nku -> Kurdish (kurmanji)\nky -> Kyrgyz\nlo -> Lao\nla -> Latin\nlv -> Latvian\nlt -> Lithuanian\nlb -> Luxembourgish\nmk -> Macedonian\nmg -> Malagasy\nms -> Malay\nml -> Malayalam\nmt -> Maltese\nmi -> Maori\nmr -> Marathi\nmn -> Mongolian\nmy -> Myanmar (burmese)\nne -> Nepali\nno -> Norwegian\nor -> Oriya\nps -> Pashto\nfa -> Persian\npl -> Polish\npt -> Portuguese\npa -> Punjabi\nro -> Romanian\nru -> Russian\nsm -> Samoan\ngd -> Scots gaelic\nsr -> Serbian\nst -> Sesotho\nsn -> Shona\nsd -> Sindhi\nsi -> Sinhala\nsk -> Slovak\nsl -> Slovenian\nso -> Somali\nes -> Spanish\nsu -> Sundanese\nsw -> Swahili\nsv -> Swedish\ntg -> Tajik\nta -> Tamil\ntt -> Tatar\nte -> Telugu\nth -> Thai\ntr -> Turkish\ntk -> Turkmen\nug -> Uighur\nuk -> Ukrainian\nur -> Urdu\nuz -> Uzbek\nvi -> Vietnamese\ncy -> Welsh\nxh -> Xhosa\nyi -> Yiddish\nyo -> Yoruba\nzu -> Zulu</b>",reply_to_message_id = message.id , parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.private &filters.command(['unset']))
async def unsetlg(client,message):
	unset(int(message.chat.id))
	await message.reply_text("**Successfully Removed Custom Default Language**",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))

@Client.on_message(filters.private &filters.command(['set']))
async def setlg(client,message):
    	    user_id = int(message.chat.id)
    	    insert(user_id)
    	    text = message.text
    	    textspit = text.split('/set')
    	    lg_code = textspit[1]
    	    if lg_code:
    	    		cd = lg_code.lower().replace(" ", "")
    	    		try:
    	    			lgcd = list[cd]
    	    		except:
    	    			await message.reply_text("**❗️ This Language Not Available in My List \n Or Check Your spelling 😉\n\nCheck Languages List With Language Code**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Star Bots Tamil" ,url="https://t.me/Star_Bots_Tamil")]]))
    	    			return
    	    		set(user_id,lgcd)
    	    		await message.reply_text(f"**Successfully Set Custom Default Language {cd}**",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))
    	    else:
    	    		await message.reply_text("**Please Use This Command with an Argument.You Can Get More Languages /list.\nFor Example :-** <code>/set Tamil</code>",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Star Bots Tamil",url = "https://t.me/Star_Bots_Tamil")]]))
