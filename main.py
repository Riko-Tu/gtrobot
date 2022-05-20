from telethon import TelegramClient

from config.runConfig import config

api_hash = config.api_hash
client = TelegramClient('anon', config.api_id, api_hash)
async def main():
    # 获取关于自己的信息
    me = await client.get_me()

    # me是一个用户对象。你可以进行完美打印
    # 任何带有stringify方法的Telegram对象:
    print(me.stringify())

    # 当你打印一些东西时，你会看到它的一个表示。
    # 您可以访问Telegram对象的所有属性
    # #点操作符。例如，要获取用户名:
    username = me.username
    print(username)
    print(me.phone)

    # 你可以打印你参与的所有对话/对话:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # 你可以给自己发信息…
    await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    await client.send_message(-100123456, 'Hello, group!')
    # 到您的联系人
    await client.send_message('+34600123123', 'Hello, friend!')
    # 或任何用户名
    await client.send_message('username', 'Testing Telethon!')

    # 当然，你可以在你的消息中使用markdown:
    message = await client.send_message(
        'me',
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )

    # 发送消息将返回您可以使用的已发送消息对象
    print(message.raw_text)

    # 如果你有一个消息对象，你可以直接回复消息
    await message.reply('Cool!')

    # ：或者发送文件、歌曲、文件、相册……
    await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # 您可以打印任何聊天的消息历史:
    async for message in client.iter_messages('me'):
        print(message.id, message.text)

        # 你也可以从消息中下载媒体!该方法将返回文件保存的路径
        if message.photo:
            path = await message.download_media()
            print('File saved to', path)  # 下载完成后打印

with client:
    client.loop.run_until_complete(main())