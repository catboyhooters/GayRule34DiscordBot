import discord
import requests
import json
import random
import io
import ntpath
import os

token = "Your token here"

commands = ["}help", "}pic", "}picture", "}gif", "}vid", "}video", "}custom", "}weird", "}w", "}w5"]

weird_tags = ["gore","cock_and_ball_torture","snuff","futanari"]

client = discord.Client()

@client.event
async def on_message(message):
	if message.content.split(" ")[0] in commands:
		if commands.index(message.content.split(" ")[0]) == 0:
			embed=discord.Embed(title="Help", description="commands:", color=0xe5a4a4)
			embed.add_field(name="}pic | }picture", value="posts random \"male_only\"-tagged picture", inline=False)
			embed.add_field(name="}vid | }video", value="posts random \"male_only\"-tagged video", inline=False)
			embed.add_field(name="}gif", value="posts random \"male_only\"-tagged gif", inline=False)
			embed.add_field(name="}custom [tags (seperated by space)]", value="posts random upload with given tags", inline=False)
			embed.add_field(name="}weird | }w", value="posts \"weird\" upload", inline=False)
			await message.channel.send(embed=embed)
		else:
			try:
				if message.channel.is_nsfw():
					await message.channel.trigger_typing()
					await post(message)
				else:
					await message.channel.send("This command only works in NSFW channels.")
			except:
				await message.channel.trigger_typing()
				await post(message)
		
async def post(message):
	
	index = commands.index(message.content.split(" ")[0])

	if index == 1 or index == 2:
		
		response = 1
		for i in range(10): 
			try:
				response = requests.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&json=1&tags=male_only+-gif+-animated+-video",
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				
				response_dict = response.json()
				valid_response_dict = []
				for i in range(len(response_dict)):
					if os.path.splitext(response_dict[i]["file_url"])[-1] in [".png", ".jpeg", ".bmp", ".jpg"]:
						valid_response_dict.append(response_dict[i])
				if(len(valid_response_dict) != 0):
				
					post = random.choice(valid_response_dict)
					print(post["file_url"])
					embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
					embed.set_footer(text="posted by: " + post["owner"])
					embed.set_image(url=post["file_url"])
					await message.channel.send(embed=embed)
				else:
					await message.channel.send("0 results for given tags")
			else:
				await message.channel.send("error")
		else:
			await message.channel.send("timeout")
	elif index == 3:
				
		response = 1
		for i in range(10): 
			try:
				response = requests.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&json=1&tags=male_only+gif",
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				
				response_dict = response.json()
				valid_response_dict = []
				for i in range(len(response_dict)):
					if os.path.splitext(response_dict[i]["file_url"])[-1] in [".gif"]:
						valid_response_dict.append(response_dict[i])
				if(len(valid_response_dict) != 0):
				
					post = random.choice(valid_response_dict)
					print(post["file_url"])
					embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
					embed.set_footer(text="posted by: " + post["owner"])
					embed.set_image(url=post["file_url"])
					await message.channel.send(embed=embed)
				else:
					await message.channel.send("0 results for given tags")
			else:
				await message.channel.send("error")
		else:
			await message.channel.send("timeout")
	elif index == 4 or index == 5:
				
		response = 1
		for i in range(10): 
			try:
				response = requests.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&json=1&tags=male_only+animated",
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				
				response_dict = response.json()
				valid_response_dict = []
				for i in range(len(response_dict)):
					if os.path.splitext(response_dict[i]["file_url"])[-1] in [".webm", ".mp4"]:
						valid_response_dict.append(response_dict[i])
				if(len(valid_response_dict) != 0):
				
					post = random.choice(valid_response_dict)
					print(post["file_url"])
					embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
					embed.set_footer(text="posted by: " + post["owner"])
					await message.channel.send(embed=embed)
					await message.channel.send(post["file_url"])
				else:
					await message.channel.send("0 results for given tags")
			else:
				await message.channel.send("error")
		else:
			await message.channel.send("timeout")
	elif index == 6:
		tags = message.content.split(" ")
		del tags[0]
		url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&json=1&tags="
		for tag in tags:
			url = url + "+" + str(tag)
		print(url)

		response = 1
		for i in range(10): 
			try:
				response = requests.get(url,
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				
				response_dict = response.json()
				post = random.choice(response_dict)
				print(post["file_url"])
				embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
				embed.set_footer(text="posted by: " + post["owner"])
				await message.channel.send(embed=embed)
				await message.channel.send(post["file_url"])
			else:
				await message.channel.send("0 results for given tags")
		else:
			print("timeout")
	elif index == 7 or index == 8:
		tags = random.sample(weird_tags, 2)
		url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=200&json=1&tags="
		for tag in tags:
			url = url + "+" + str(tag)
		print(url)

		response = 1
		for i in range(10): 
			try:
				response = requests.get(url,
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				
				response_dict = response.json()
				post = random.choice(response_dict)
				print(post["file_url"])
				embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
				embed.set_footer(text="posted by: " + post["owner"])
				await message.channel.send(embed=embed)
				await message.channel.send(post["file_url"])
			else:
				await message.channel.send(":man_cartwheeling:\n:manual_wheelchair::person_golfing:")
		else:
			print("timeout")
	elif index == 9:
		tags = random.sample(weird_tags, 2)
		url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=200&json=1&tags="
		for tag in tags:
			url = url + "+" + str(tag)
		print(url)

		response = 1
		for i in range(10): 
			try:
				response = requests.get(url,
										headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},
										timeout = 1)
				break
			except:
				print("timeout")
		if response != 1:
			print("response")
			if response.status_code == 200 and response.text != "":
				try:
					response_dict = response.json()
					posts = random.sample(response_dict, 5)
					for post in posts:
							embed=discord.Embed(color=0xaae5a3, title="rule34.xxx", url="https://rule34.xxx/index.php?page=post&s=view&id="+str(post["id"]))
							embed.set_footer(text="posted by: " + post["owner"])
							await message.channel.send(embed=embed)
							await message.channel.send(post["file_url"])
				except:
					await message.channel.send(":man_cartwheeling:\n:manual_wheelchair::person_golfing:")
			else:
				await message.channel.send(":man_cartwheeling:\n:manual_wheelchair::person_golfing:")
		else:
			print("timeout")
				

client.run(token)
