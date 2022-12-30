
import io
import discord
from PIL import Image, ImageDraw, ImageFont
from discord import ApplicationCommandInteraction
from discord.ext import commands

from database.models import LevelUser

class LevelCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.slash_command(name='level', description='Zeigt dir dein Level an.')
	async def level(self, ctx: ApplicationCommandInteraction):
		await ctx.defer(hidden=True)
		level_user = await LevelUser(ctx.author.id).load()

		img = Image.new('RGB', (500, 140), color = (15, 15, 15))
		draw = ImageDraw.Draw(img)
		font_big = ImageFont.truetype('assets/Rubik-Black.ttf', 50)
		font_normal = ImageFont.truetype('assets/Rubik-Regular.ttf', 24)


		draw.text((10, 10), f'Level {level_user.get_level()}', font=font_big, fill=(255, 255, 255))
		draw.text((10, 70), f'XP: {level_user.xp}/{level_user.get_xp_for_next_level()}', font=font_normal, fill=(255, 255, 255))
		draw.text((10, 100), f'Nächstes Level in {level_user.get_xp_for_next_level() - level_user.xp} XP', font=font_normal, fill=(255, 255, 255))

		avatar_data = await ctx.author.avatar_url.read()
		avatar = Image.open(io.BytesIO(avatar_data))
		avatar = avatar.resize((100, 100))
		img.paste(avatar, (380, 20))

		img.save('temp-level.png')

		await ctx.respond(file=discord.File('temp-level.png'), hidden=True)

def setup(bot: commands.Bot):
	bot.add_cog(LevelCommand(bot))