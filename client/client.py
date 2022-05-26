
from telethon import TelegramClient
from config.runConfig import config




chatlist = [-1001500300314,-1001480532910 ,401234709]
class client:
    def __int__(self):
      self.api_id = config.api_id
      self.api_hash = config.api_hash
      self.client = TelegramClient('anon', self.api_id, self.api_hash,session="session")
      self.me = await self.client.get_me()

    async def getclient(self):
       return self.client

    def get_info(self):
      return  self.me.stringify()

    def get_username(self):
      return self.me.username

    def get_name(self):
      return self.me.first_name

    def get_phone(self):
      return self.me.phone

    def get_userID(self):
      return self.me.id

    def get_hash(self):
      return self.me.access_hash

    def send_messge(self):
      pass

    def get_dictchat(self):
        chatgroup={}
        async for dialog in self.client.iter_dialogs():
            chatgroup[dialog.name]= dialog.id
        return chatgroup


    def msg_to_me(self,):
        await self.client.send_message("me",)


    def msg_to_chat(self,chat):
        """
        chat: 支持chatid,username,带+手机号
        """
        await self.client.send_message(entity=chat,)

    async def chat_history(self,chat,limit):
        async for message in self.client.iter_messages(chat,limit=limit):
            print(message.id, message.text)


    def evnet(self):
        print(self.get_dictchat())
        chatlist = [-1001500300314, -1001480532910, 401234709]
        for id in chatlist:
            self.chat_history(id,10)

    def run(self):
        self.client.loop.run_until_complete(self.evnet())

client.evnet()