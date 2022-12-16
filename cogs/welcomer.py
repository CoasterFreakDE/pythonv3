import discord
from discord.ext import commands


class Welcomer(commands.Cog):

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.get_channel(658960248345853955)

		embed = discord.Embed(title='Willkommen auf unserem Server!',
		                      description=f'Willkommen, {member.mention}! Wir hoffen, du hast Spaß auf unserem Server!\n\n'
		                                  f'Du bist der {len(member.guild.members)}. Nutzer auf unserem Server!',
		                      color=0x00ff00)
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(Welcomer(bot))