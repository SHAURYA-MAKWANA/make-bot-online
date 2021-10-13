import os
from webserver import keep_alive
import flask
import discord
from discord.ext import commands

client = commands.AutoShardedBot(commands.when_mentioned_or('$'))

print("bot is online")

keep_alive()
client.run("token")