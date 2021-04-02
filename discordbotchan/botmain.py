import os
import discord
import asyncio
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
    await client.change_presence(activity=discord.Game(name="殻"))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '!test':
        await message.channel.send('ちゃんと動いてるよ！')

    if message.content == '0':
        sengen_channel_id = 813989805120946206
        channel_sent = client.get_channel(813992895332876309)
        m = '⚔' + message.author.display_name + 'さんが凸を開始したよ'
        embed = discord.Embed(title=m, description='※このメッセージは10秒後に消えるよ👻', color=discord.Colour.from_rgb(255, 0, 0))
        if message.channel.id == sengen_channel_id:
            await channel_sent.send(embed=embed, delete_after=10.0)

    if message.content == '??help':
        line = '--------------------------------------\n'
        a = '🔸凸宣言・報告・希望のやり方 : ?流れ''\n'
        b = '🔸凸宣言のキャンセルしたい : ?宣言''\n'
        c = '🔸報告済みの凸を消したい : ?凸''\n'
        d = '🔸現在の周数を修正したい : ?周数''\n'
        e = '🔸現在のボスを修正したい : ?ボス''\n'
        f = '🔸その他: <@&717295065902481488><@&717296038230229003>まで'
        embed = discord.Embed(title='🥚生卵HELP🥚',
                              description='該当するコマンドを入力してね！''\n''`※このメッセージは🗑を押して消してね`''\n' + line + a + b + c + d + e + f,
                              color=discord.Colour.gold())
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    elif message.content == '?流れ':
        a = '**🔸凸宣言**''\n''チャンネル：<#813989805120946206>''\n'
        b = '**🔸凸報告**''\n''チャンネル：<#813989860037754900>''\n'
        c = '**🔸凸希望**''\n''チャンネル：<#800966966167863326>''\n'
        kieruyo = '`※このメッセージは🗑を押して消してね`'
        embed = discord.Embed(title='凸宣言・報告・希望のやり方', description=a + b + c + kieruyo)
        embed.set_image(
            url='https://media.discordapp.net/attachments/818646643842613248/819077983956369468/nagare3.png?width=1410&height=936')
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    elif message.content == '?宣言':
        a = 'チャンネル：<#813989805120946206>''\n'
        b = '書き込み：キャンセル'
        kieruyo = '\n''`※このメッセージは🗑を押して消してね`'
        embed = discord.Embed(title='凸宣言のキャンセル方法', description=a + b + kieruyo)
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    elif message.content == '?凸':
        a = 'チャンネル：<#813989860037754900>''\n'
        b = '書き込み：元に戻す'
        kieruyo = '\n''`※このメッセージは🗑を押して消してね`'
        embed = discord.Embed(title='(報告済みの)凸の取り消し方', description=a + b + kieruyo)
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    elif message.content == '?周数':
        a = 'チャンネル：<#813989860037754900>''\n'
        b = '書き込み：/correct + 周数''\n'
        c = '例）35周目に直す → `/correct 35`'
        kieruyo = '\n''`※このメッセージは🗑を押して消してね`'
        embed = discord.Embed(title='周数の修正方法', description=a + b + c + kieruyo)
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    elif message.content == '?ボス':
        a = 'チャンネル：<#813989860037754900>''\n'
        b = '書き込み：/correct_boss + ボス番号''\n'
        c = '例）ワイバーン(1ボス)に直す→ `/correct_boss 1`'
        kieruyo = '\n''`※このメッセージは🗑を押して消してね`'
        embed = discord.Embed(title='現在のボスの修正方法', description=a + b + c + kieruyo)
        msg = await message.channel.send(embed=embed, delete_after=61.0)
        dust = '🗑'
        await msg.add_reaction(dust)
        await asyncio.sleep(3)
        await message.delete()

        def reaction_check(reaction, user):
            are_same_messages = (reaction.message.channel.id == msg.channel.id
                                 and reaction.message.id == msg.id
                                 and user.id == message.author.id
                                 and str(reaction.emoji) == '🗑')
            return are_same_messages

        try:
            # wait_for reaction_addを15秒間待ってリアクションが押された際はreaction_checkの関数で確認する。
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            pass
        else:
            # 時間切れにならずかつreaction_checkがあってると返した時はメッセージを削除する。(リアクションが押された)
            await msg.delete()

    if message.content == '!ok':
        # チャンネルの取得
        channel = client.get_channel(818363498559963137)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441352416591894)
        channel_sent = client.get_channel(818363498559963137)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        gozen_role = channel_sent.guild.get_role(827354617674596352)
        gozen_member = list(set(channel_sent.members) & set(gozen_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yu_role = channel_sent.guild.get_role(827355038930173972)
        yu_member = list(set(channel_sent.members) & set(yu_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in gozen_member])
        output3 = '\n''・'.join([member.display_name for member in hiru_member])
        output4 = '\n''・'.join([member.display_name for member in yu_member])
        output5 = '\n''・'.join([member.display_name for member in yoru_member])
        output6 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝(5:00~8:00)', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> 🏞午前️(8:00~12:00)', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼(12:00~17:00)', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🌆夕(17:00~21:00)', value='```''・' + output4 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜(21:00~24:00)', value='```''・' + output5 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜(24:00~)', value='```''・' + output6 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 2日目分
        channel = client.get_channel(818363587029499924)
        edit_message = await channel.fetch_message(818441371312324648)
        channel_sent = client.get_channel(818363587029499924)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        gozen_role = channel_sent.guild.get_role(827354617674596352)
        gozen_member = list(set(channel_sent.members) & set(gozen_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yu_role = channel_sent.guild.get_role(827355038930173972)
        yu_member = list(set(channel_sent.members) & set(yu_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in gozen_member])
        output3 = '\n''・'.join([member.display_name for member in hiru_member])
        output4 = '\n''・'.join([member.display_name for member in yu_member])
        output5 = '\n''・'.join([member.display_name for member in yoru_member])
        output6 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝(5:00~8:00)', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> 🏞午前️(8:00~12:00)', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼(12:00~17:00)', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🌆夕(17:00~21:00)', value='```''・' + output4 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜(21:00~24:00)', value='```''・' + output5 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜(24:00~)', value='```''・' + output6 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 3日目分
        channel = client.get_channel(818363661743161355)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441382946668545)
        channel_sent = client.get_channel(818363661743161355)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        gozen_role = channel_sent.guild.get_role(827354617674596352)
        gozen_member = list(set(channel_sent.members) & set(gozen_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yu_role = channel_sent.guild.get_role(827355038930173972)
        yu_member = list(set(channel_sent.members) & set(yu_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in gozen_member])
        output3 = '\n''・'.join([member.display_name for member in hiru_member])
        output4 = '\n''・'.join([member.display_name for member in yu_member])
        output5 = '\n''・'.join([member.display_name for member in yoru_member])
        output6 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝(5:00~8:00)', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> 🏞午前️(8:00~12:00)', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼(12:00~17:00)', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🌆夕(17:00~21:00)', value='```''・' + output4 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜(21:00~24:00)', value='```''・' + output5 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜(24:00~)', value='```''・' + output6 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 4日目用
        channel = client.get_channel(818363720757149757)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441394850234369)
        channel_sent = client.get_channel(818363720757149757)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        gozen_role = channel_sent.guild.get_role(827354617674596352)
        gozen_member = list(set(channel_sent.members) & set(gozen_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yu_role = channel_sent.guild.get_role(827355038930173972)
        yu_member = list(set(channel_sent.members) & set(yu_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in gozen_member])
        output3 = '\n''・'.join([member.display_name for member in hiru_member])
        output4 = '\n''・'.join([member.display_name for member in yu_member])
        output5 = '\n''・'.join([member.display_name for member in yoru_member])
        output6 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝(5:00~8:00)', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> 🏞午前️(8:00~12:00)', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼(12:00~17:00)', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🌆夕(17:00~21:00)', value='```''・' + output4 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜(21:00~24:00)', value='```''・' + output5 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜(24:00~)', value='```''・' + output6 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        # 5日目用
        channel = client.get_channel(818363767812915280)
        # メッセージの取得
        edit_message = await channel.fetch_message(818441405630382080)
        channel_sent = client.get_channel(818363767812915280)
        asa_role = channel_sent.guild.get_role(765558965152776224)
        asa_member = list(set(channel_sent.members) & set(asa_role.members))
        gozen_role = channel_sent.guild.get_role(827354617674596352)
        gozen_member = list(set(channel_sent.members) & set(gozen_role.members))
        hiru_role = channel_sent.guild.get_role(765559103317082153)
        hiru_member = list(set(channel_sent.members) & set(hiru_role.members))
        yu_role = channel_sent.guild.get_role(827355038930173972)
        yu_member = list(set(channel_sent.members) & set(yu_role.members))
        yoru_role = channel_sent.guild.get_role(779001072995794985)
        yoru_member = list(set(channel_sent.members) & set(yoru_role.members))
        shinya_role = channel_sent.guild.get_role(765559170631991306)
        shinya_member = list(set(channel_sent.members) & set(shinya_role.members))
        output1 = '\n''・'.join([member.display_name for member in asa_member])
        output2 = '\n''・'.join([member.display_name for member in gozen_member])
        output3 = '\n''・'.join([member.display_name for member in hiru_member])
        output4 = '\n''・'.join([member.display_name for member in yu_member])
        output5 = '\n''・'.join([member.display_name for member in yoru_member])
        output6 = '\n''・'.join([member.display_name for member in shinya_member])
        line = '----------------------------'
        embed = discord.Embed(title="(１日目)時間帯別メンバー表", description=line)
        embed.add_field(name='> 🐔朝(5:00~8:00)', value='```''・' + output1 + '```' + line, inline=False)
        embed.add_field(name='> 🏞午前️(8:00~12:00)', value='```''・' + output2 + '```' + line, inline=False)
        embed.add_field(name='> ☀️昼(12:00~17:00)', value='```''・' + output3 + '```' + line, inline=False)
        embed.add_field(name='> 🌆夕(17:00~21:00)', value='```''・' + output4 + '```' + line, inline=False)
        embed.add_field(name='> 🌙夜(21:00~24:00)', value='```''・' + output5 + '```' + line, inline=False)
        embed.add_field(name='> 🦇深夜(24:00~)', value='```''・' + output6 + '```' + line, inline=False)
        await edit_message.edit(content=None, embed=embed)
        await asyncio.sleep(5)
        await message.delete()

client.run(TOKEN)
