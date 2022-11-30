import discord
from discord.ext import commands


class SetupCommand(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.slash_command(base_name='setup', name='userinfo', description='Setup the userinfo command')
	async def setup_userinfo_command(self, ctx):
		await ctx.respond('Click the button to get your user info', components=[
			discord.Button(label='User Info', custom_id='userinfo-btn')
		])


def setup(bot):
	bot.add_cog(SetupCommand(bot))