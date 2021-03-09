import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await client.change_presence(activity=discord.Game(name="から"))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '!ok':
        # チャンネルの取得
        channel = client.get_channel(818363498559963137)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441352416591894)
        channel_sent = client.get_channel(818363498559963137)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in hiru_member])
        output3 = '\n''・'.join([member.display_name for member in yoru_member])
        output4 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝活勢', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼勢', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜勢', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜勢', value='```''・' + output4 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 2日目分
        channel = client.get_channel(818363587029499924)
        edit_message = await channel.fetch_message(818441371312324648)
        channel_sent = client.get_channel(818363587029499924)
        asa_role = channel_sent.guild.get_role(818309056421822464)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        hiru_role = channel_sent.guild.get_role(818309283590570035)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yoru_role = channel_sent.guild.get_role(818309373574774795)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(818309540415537204)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in hiru_member])
        output3 = '\n''・'.join([member.display_name for member in yoru_member])
        output4 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '------------------------------'
        embed = discord.Embed(title="(2日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝活勢', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼勢', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜勢', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜勢', value='```''・' + output4 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 3日目分
        channel = client.get_channel(818363661743161355)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441382946668545)
        channel_sent = client.get_channel(818363661743161355)
        asa_role = channel_sent.guild.get_role(818358562446639115)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        hiru_role = channel_sent.guild.get_role(818358447346810880)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yoru_role = channel_sent.guild.get_role(818358372641931294)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(818358306937765898)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in hiru_member])
        output3 = '\n''・'.join([member.display_name for member in yoru_member])
        output4 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(3日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝活勢', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼勢', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜勢', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜勢', value='```''・' + output4 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 4日目用
        channel = client.get_channel(818363720757149757)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441394850234369)
        channel_sent = client.get_channel(818363720757149757)
        asa_role = channel_sent.guild.get_role(818359476968620052)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        hiru_role = channel_sent.guild.get_role(818358785013710848)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yoru_role = channel_sent.guild.get_role(818358705829314561)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(818358640977248266)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in hiru_member])
        output3 = '\n''・'.join([member.display_name for member in yoru_member])
        output4 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(4日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝活勢', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼勢', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜勢', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜勢', value='```''・' + output4 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 5日目用
        channel = client.get_channel(818363767812915280)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441405630382080)
        channel_sent = client.get_channel(818363767812915280)
        asa_role = channel_sent.guild.get_role(818359940392419339)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        hiru_role = channel_sent.guild.get_role(818359887288467477)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yoru_role = channel_sent.guild.get_role(818359823677915176)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(818359757966540822)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in hiru_member])
        output3 = '\n''・'.join([member.display_name for member in yoru_member])
        output4 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(5日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝活勢', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼勢', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜勢', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜勢', value='```''・' + output4 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)


client.run(TOKEN)
