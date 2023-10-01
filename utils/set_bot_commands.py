from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start up the bot"),
            types.BotCommand("help", "Gives help (under construction)"),
            types.BotCommand("weather", "'What's the weather?' Find out here!")


        ]
    )