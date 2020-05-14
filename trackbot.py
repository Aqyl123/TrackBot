import discord
import asyncio
import shippo 
import datetime

shippo.config.api_key = 'API KEY'
token = 'DISCORD BOT TOKEN'
client = discord.Client()

@client.event
async def on_ready():
    print('--------------------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('!'):
        cmd = message.content.split()[0].lower()[1:]
        args = message.content.split()[1:]
        packageTrack = ' '.join(args)

        if cmd == 'usps':
            tracking_number = packageTrack
            carrier_token = 'usps'
            tracking = shippo.Track.get_status(carrier_token, tracking_number)
            d1 = datetime.datetime.strptime(tracking['tracking_status']['status_date'], "%Y-%m-%dT%H:%M:%SZ")
            new_format = "%m-%d-%Y" + " at " + "%H:%M"

            uspsStatus = tracking['tracking_status']['status_details'] + " - " + tracking['tracking_status']['status']
            uspsCity = tracking['tracking_status']['location']['city']
            uspsState = tracking['tracking_status']['location']['state']
            uspsZip = tracking['tracking_status']['location']['zip']
            uspsDate = d1.strftime(new_format)

            embed = discord.Embed(title="Tracking", color=0x1E90FF)
            embed.set_author(name="USPS Tracking", url="https://tools.usps.com/go/TrackConfirmAction?tLabels={}".format(str(tracking_number)), icon_url="https://www.freepnglogos.com/uploads/usps-png-logo/bridgeport-apartments-usps-png-logo-2.png")
            embed.set_thumbnail(url="https://www.freepnglogos.com/uploads/usps-png-logo/bridgeport-apartments-usps-png-logo-2.png")
            embed.add_field(name="Tracking Number: ", value="{}".format(str(tracking_number)), inline=False)
            embed.add_field(name="Status: ", value="{}".format(str(uspsStatus)), inline=False)
            embed.add_field(name="Date & Time: ", value="{}".format(str(uspsDate)), inline=False)
            embed.add_field(name="Location: ", value="{}".format(str(uspsCity) + ", " + str(uspsState) + " " + str(uspsZip)), inline=False)
            embed.set_footer(icon_url="https://i.imgur.com/O5PcNtt.png", text="TRACKBOT | Made by Aqyl#0093")
            await message.channel.send(embed=embed)

        if cmd == 'ups':
            tracking_number = packageTrack
            carrier_token = 'ups'
            tracking = shippo.Track.get_status(carrier_token, tracking_number)
            d1 = datetime.datetime.strptime(tracking['tracking_status']['status_date'], "%Y-%m-%dT%H:%M:%SZ")
            new_format = "%m-%d-%Y" + " at " + "%H:%M"

            upsStatus = tracking['tracking_status']['status_details'] + " - " + tracking['tracking_status']['status']
            upsCity = tracking['tracking_status']['location']['city']
            upsState = tracking['tracking_status']['location']['state']
            upsZip = tracking['tracking_status']['location']['zip']
            upsDate = d1.strftime(new_format)

            embed = discord.Embed(title="Tracking", color=0x8B4513)
            embed.set_author(name="UPS Tracking", url="https://www.ups.com/WebTracking?loc=en_US&Requester=DAN&tracknum={}".format(str(tracking_number)), icon_url="https://pluspng.com/img-png/new-ups-logo-png-ups-logo-logotype-3410.png")
            embed.set_thumbnail(url="https://pluspng.com/img-png/new-ups-logo-png-ups-logo-logotype-3410.png")
            embed.add_field(name="Tracking Number: ", value="{}".format(str(tracking_number)), inline=False)
            embed.add_field(name="Status: ", value="{}".format(str(upsStatus)), inline=False)
            embed.add_field(name="Date & Time: ", value="{}".format(str(upsDate)), inline=False)
            embed.add_field(name="Location: ", value="{}".format(str(upsCity) + ", " + str(upsState) + " " + str(upsZip)), inline=False)
            embed.set_footer(icon_url="https://i.imgur.com/O5PcNtt.png", text="TRACKBOT | Made by Aqyl#0093")
            await message.channel.send(embed=embed)

        if cmd == 'fedex':
            tracking_number = packageTrack
            carrier_token = 'fedex'
            tracking = shippo.Track.get_status(carrier_token, tracking_number)
            d1 = datetime.datetime.strptime(tracking['tracking_status']['status_date'], "%Y-%m-%dT%H:%M:%SZ")
            new_format = "%m-%d-%Y" + " at " + "%H:%M"

            fedexStatus = tracking['tracking_status']['status_details'] + " - " + tracking['tracking_status']['status']
            fedexCity = tracking['tracking_status']['location']['city']
            fedexState = tracking['tracking_status']['location']['state']
            fedexZip = tracking['tracking_status']['location']['zip']
            fedexDate = d1.strftime(new_format)

            embed = discord.Embed(title="Tracking", color=0x4B0082)
            embed.set_author(name="FedEx Tracking", url="http://fedex.com/apps/fedextrack/?action=track&trackingnumber={}".format(str(tracking_number)), icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/FedEx_Corporation_-_2016_Logo.svg/1200px-FedEx_Corporation_-_2016_Logo.svg.png")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/FedEx_Corporation_-_2016_Logo.svg/1200px-FedEx_Corporation_-_2016_Logo.svg.png")
            embed.add_field(name="Tracking Number: ", value="{}".format(str(tracking_number)), inline=False)
            embed.add_field(name="Status: ", value="{}".format(str(fedexStatus)), inline=False)
            embed.add_field(name="Date & Time: ", value="{}".format(str(fedexDate)), inline=False)
            embed.add_field(name="Location: ", value="{}".format(str(fedexCity) + ", " + str(fedexState) + " " + str(fedexZip)), inline=False)
            embed.set_footer(icon_url="https://i.imgur.com/O5PcNtt.png", text="TRACKBOT | Made by Aqyl#0093")
            await message.channel.send(embed=embed)

client.run(token)
