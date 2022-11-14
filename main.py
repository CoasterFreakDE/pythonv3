import logging
import os
from pathlib import Path

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('BOT-MAIN')

bot = commands.Bot(
	command_prefix=None,
	intents=discord.Intents.default(),
	activity=discord.Activity(type=discord.ActivityType.playing, name='Hello World!'),
	status=discord.Status.online,
	sync_commands=True,
	delete_not_existing_commands=True
)

if __name__ == '__main__':
	log.info('Starting bot...')
	cogs = [p.stem for p in Path('cogs').glob('**/*.py') if not p.name.startswith('__')]
	log.info('Loading %d extensions...', len(cogs))

	for cog in cogs:
		bot.load_extension(f'cogs.{cog}')
		log.info('Loaded %s', cog)

	token = os.getenv('BOT_TOKEN')
	bot.run(token)
