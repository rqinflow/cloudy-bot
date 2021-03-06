import discord
from discord.ext import commands
import random
import os
import json
from firebase_admin import storage

class Chroma(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def logos(self, ctx):
        stored_guild_id = 694010548605550675
        if ctx.guild.id == stored_guild_id:
            em = discord.Embed(title="logos", description="click [**here**]() for the chroma logos! <3", color=0x303136)
            await ctx.author.send(embed=em)
            await ctx.reply("i sent you our logos!")

    @commands.command()
    async def hi(self, ctx):
        name = ctx.message.author.mention
        await ctx.send(f'hi {name}! i hope ur having a great day ily<3')

    @commands.command()
    async def memberinfo(self, ctx, user:discord.Member=None):
        stored_guild_id = 694010548605550675
        display = user.display_name
        sheher = discord.utils.find(lambda r: r.name == 'she/her', ctx.message.guild.roles)
        theythem = discord.utils.find(lambda r: r.name == 'they/them', ctx.message.guild.roles)
        shethey = discord.utils.find(lambda r: r.name == 'she/they', ctx.message.guild.roles)
        hethey = discord.utils.find(lambda r: r.name == 'he/they', ctx.message.guild.roles)
        hehim = discord.utils.find(lambda r: r.name == 'he/him', ctx.message.guild.roles)
        any = discord.utils.find(lambda r: r.name == 'any pronouns', ctx.message.guild.roles)
        role1 = discord.utils.find(lambda r: r.name == 'after effects', ctx.message.guild.roles)
        role2 = discord.utils.find(lambda r: r.name == 'videostar', ctx.message.guild.roles)
        role3 = discord.utils.find(lambda r: r.name == 'alight motion', ctx.message.guild.roles)
        role4 = discord.utils.find(lambda r: r.name == 'cute cut pro', ctx.message.guild.roles)
        role5 = discord.utils.find(lambda r: r.name == 'sony vegas pro', ctx.message.guild.roles)
        if user is None:
            user = ctx.message.author
        else:
            pass
        if ctx.guild.id == stored_guild_id:
            title1 = f"chroma member | {display}"
        else:
            title1 = f"editing-info about {display}"
        if role1 in user.roles:
            program = "after effects"
            if role2 in user.roles:
                program = "after effects and video star"
            elif role5 in user.roles:
                program = "after effects and sony vegas pro"
            elif role3 in user.roles:
                program = "after effects and alight motion"
        if role1 not in user.roles:
            if role2 in user.roles:
                program = "video star"
                if role3 in user.roles:
                    program = "video star and alight motion"
                    if role4 in user.roles:
                        program = "video star, alight motion and cute cut pro"
            elif role3 in user.roles:
                program = "alight motion"
                if role4 in user.roles:
                    program = "alight motion and cute cut pro"
            elif role4 in user.roles:
                program = "cute cut pro"
            elif role5 in user.roles:
                program = "sony vegas pro"
            else:
                program = "an unspecified editing software"
        embed = discord.Embed(title="chroma member", description=f"{user.display_name} makes their edits using {program}", color=0xFF90FB)
        if sheher in user.roles:
            prns = "she/her"
            prn1 = "she uses"
            prn2 = "her"
        elif hehim in user.roles:
            prns = "he/him"
            prn1 = "he uses"
            prn2 = "his"
        elif shethey in user.roles:
            prns = "she/they"
            prn1 = "they use"
            prn2 = "her"
        elif hethey in user.roles:
            prns = "he/they"
            prn1 = "they use"
            prn = "his"
        elif theythem in user.roles:
            prns = "they/them"
            prn1 = "they use"
            prn2 = "their"
        elif any in user.roles:
            prns = "any pronouns"
            prn1 = "they use"
            prn2 = "their"
        else:
            prns = "not specified"
            prn1 = "they use"
            prn2 = "their"
        embed = discord.Embed(title=title1, 
        description=f"??? {display}'s prounouns are {prns}\n??? {prn1} {program} to edit", color=0xFF90FB)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_image(url="https://media.discordapp.net/attachments/804482120671821865/855135807697321994/2021-06-12_18.40.11.png?width=1191&height=670")
        if "|" in display:
            list = display.split("|")
            name1 = list[0]
            name = name1.replace(" ", "")
            username = list[1]
            acc = username.replace(" ", "")
            embed = discord.Embed(title=title1, 
            description=f"??? {name}'s pronouns are {prns}\n??? {prn1} {program} to edit\n??? [click here to go to {prn2} instagram](https://instagram.com/{acc})\n??? {name} made the edit below!", color=0xFF90FB)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_image(url="https://media.discordapp.net/attachments/804482120671821865/855135807697321994/2021-06-12_18.40.11.png?width=1191&height=670")
            await ctx.reply(embed=embed)
            message = await ctx.send(f"react to this message if you want to see one of {name}'s edits!")
            await message.add_reaction("???")
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["???"] and reaction.message == message
            confirmation = await self.client.wait_for("reaction_add", check=check) 
            if confirmation:
                await message.delete()
                await ctx.send(f"https://rqinflow.com/{acc}")
        else:
            await ctx.reply(embed=embed)

    @commands.command(aliases=["edit"])
    async def edits(self, ctx):
        bucket = storage.bucket()
        edits = []
        blobs = list(bucket.list_blobs())
        for blob in blobs:
            first = blob.name
            second = first.replace("files/", "")
            name = second.replace(".mp4", "")
            edits.append(name)
        edit = random.choice(edits)
        await ctx.send("https://cloudy.rqinflow.com/" + edit)

    @commands.command()
    @commands.has_role("Server Booster")
    async def claimperks(self, ctx):
        guild = 694010548605550675
        if ctx.guild.id == guild:
            embed = discord.Embed(title="resources", color=0xDECAB2)
            embed.add_field(name="starrys.aep resources", value="", inline=False)
            embed.add_field(name="grandily doodles", value="", inline=False)
            embed.add_field(name="qtplum resources", value="", inline=False)
            embed.add_field(name="lovinasbutera colorings", value="", inline=False)
            embed.add_field(name="blqckthorns shakes and colorings", value="", inline=False)
            embed.add_field(name="_raven.mp4 turbs", value="", inline=False)
            await ctx.author.send(embed=embed)
            await ctx.reply("check your dms!")
        else:
            return



def setup(client):
    client.add_cog(Chroma(client))