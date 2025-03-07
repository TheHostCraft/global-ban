import discord
from discord.ext import commands
from discord.commands import slash_command, user_command
import yaml
import os

class GlobalBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('./configs/glob-ban.yaml', 'r') as file:
            self.config = yaml.safe_load(file)
        self.required_roles = self.config['required_roles']
        self.main_server_id = self.config['main_server_id']
        self.global_ban_servers = self.config['global_ban_servers']

    async def has_required_role(self, user):
        main_guild = self.bot.get_guild(self.main_server_id)
        member = main_guild.get_member(user.id)
        if member:
            for role in member.roles:
                if role.id in self.required_roles:
                    return True
        return False

    @slash_command()
    async def global_ban(self, ctx, user_id: int, reason: str = None):
        if await self.has_required_role(ctx.author):
            user = discord.Object(id=user_id)
            for server_id in self.global_ban_servers:
                guild = self.bot.get_guild(server_id)
                if guild:
                    await guild.ban(user, reason=reason)
            await ctx.respond(f'User with ID {user_id} has been globally banned.\n-# ©TheHostCraft')
        else:
            await ctx.respond('You do not have the required role to perform this action.\n-# ©TheHostCraft')

    @slash_command()
    async def global_unban(self, ctx, user_id: int):
        if await self.has_required_role(ctx.author):
            user = discord.Object(id=user_id)
            for server_id in self.global_ban_servers:
                guild = self.bot.get_guild(server_id)
                if guild:
                    await guild.unban(user)
            await ctx.respond(f'User with ID {user_id} has been globally unbanned.\n-# ©TheHostCraft')
        else:
            await ctx.respond('You do not have the required role to perform this action.\n-# ©TheHostCraft')

    @user_command(name="Global Ban")
    async def global_ban_app(self, ctx, user: discord.User):
        if await self.has_required_role(ctx.author):
            for server_id in self.global_ban_servers:
                guild = self.bot.get_guild(server_id)
                if guild:
                    await guild.ban(user)
            await ctx.respond(f'User {user} has been globally banned.\n-# ©TheHostCraft')
        else:
            await ctx.respond('You do not have the required role to perform this action.\n-# ©TheHostCraft')

    @user_command(name="Global Unban")
    async def global_unban_app(self, ctx, user: discord.User):
        if await self.has_required_role(ctx.author):
            for server_id in self.global_ban_servers:
                guild = self.bot.get_guild(server_id)
                if guild:
                    await guild.unban(user)
            await ctx.respond(f'User {user} has been globally unbanned.\n-# ©TheHostCraft')
        else:
            await ctx.respond('You do not have the required role to perform this action.\n-# ©TheHostCraft')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is ready.')

def setup(bot):
    bot.add_cog(GlobalBan(bot))