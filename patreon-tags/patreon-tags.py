# « »
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

tiers = [
	"wt", #wobbless
	"rwt", # rainbow wobbles
	"uct", #ultimate clock
	"mwt", #mega wobbles
	"st" # sponsor
]

class Patreon(commands.Cog):
	def __init__(self, bot):
 		self.bot = bot

	@commands.command()
	@checks.thread_only()
	@checks.has_permissions(PermissionLevel.SUPPORTER)
	async def ptag(self, ctx, *, tier: str=None):
	   """Tag the thread"""
	   if tier is None:
		   return await ctx.send("Not possible")
		tier = tier.lower()
		if tier in patreon_tiers:
			await ctx.thread.edit(name=f"«{tier}»-{ctx.thread.recipient}",
								 reason=f"Modification of thread name by {ctx.author}")
			await ctx.send("Done")


async def setup(bot):
	await bot.add_cog(Patreon(bot))
