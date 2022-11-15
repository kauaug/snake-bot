from discord.ext.commands import errors
from discord.ext import commands


class IntentionalError(errors.CommandError):
    """Exception when there is a conflict caused by the bot, which did not consider a user error.

    This inherited from :exc:`CommandError`.
    """
    pass


class Errors(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, errors.CommandError):
            return await ctx.message.reply(str(error))
        raise error


async def setup(bot: commands.Bot):
    await bot.add_cog(Errors(bot))
