import discord
import time
import random

client = discord.Client()
token="NzE2NjI2NDUxMTc2MDk1ODQz.XtOgZA.NoOju6FJLGCRHL8sF3K1dcECLzc"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Hello World")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    check = 1
    week = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    color = ["-","+","---"," "]
    if message.content.startswith("!hello"):
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send('```diff\n-Hello\n-I am Hello World Bot\n-I will tell you how to make hello world program\n-If you do not how to use me, send me -help'+"\n"
                                   +"```"
                                   +"```"+"cs"+"\n"
                                   +"'Today is "+("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n] + "'"+"\n"
                                   +"'This time is "+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                   +"'```")
    if message.content.startswith("!help"):
        await message.channel.send("```diff\n-Write '!' + programming language that you want\n-I can tell you everything on this list\n-python\n-java\n-c/c++\n-c#\n-html\n-go```")
    if message.content.startswith("!time"):
        now = time.localtime()
        await message.channel.send("```cs"+"\n"+"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))+"'```")
    if message.content.startswith("!day"):
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'```")
    if message.content.startswith("!now"):
         now = time.localtime()
         n = time.localtime().tm_wday
         await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'"+"\n"
                                    +"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                    +"'```")
    if message.content.startswith("!python"):
        await message.channel.send('```python\nprint("Hello World")```')
    if message.content.startswith("!java"):
        await message.channel.send('```java\npublic class HelloWorld {\n    public static void main(String args[]) {\n        System.out.println("Hello World");\n    }\n}```')
    if message.content.startswith("!html"):
        await message.channel.send('```html\n<html>\n  <body>\n    hello world!\n  </body>\n</html>```')
    if message.content.startswith("!c++"):
        await message.channel.send('```c++\n#include <iostream>\n\nusing namespace std;\n\nint main()\n{\n	cout << "Hello World" << endl;\n	return 0;\n}```')
    elif message.content.startswith("!c#"):
        await message.channel.send('```c\nusing System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Text;\nusing System.Threading.Tasks;\n\nnamespace ConsoleApp1\n{\n    class Program\n    {\n        static void Main(string[] args)\n        {\n            Console.WriteLine("Hello World");\n        }\n    }\n}```')
    elif message.content.startswith("!c"):
        await message.channel.send('```c\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n\n    return 0;\n}```')
    if message.content.startswith("!go"):
        await message.channel.send('```go\npackage main\n\nimport "fmt"\n\nfunc main()\n{\n	fmt.Println("Hello, World")\n}```')
    if message.content.startswith("!파괘"):
        await message.channel.send("```diff"+"\n"+"나를 막는 것은 무엇이든지..."+"\n"+"-파.괘.한.다."+ "```")
    if message.content.startswith("!와"):
        o = random.randint(0,1)
        if o == 0:
            p = random.randint(0,3)
            await message.channel.send("```diff"+"\n"+color[p]+"샌즈!"+"```")
        if o == 1:
            p = random.randint(0,1)
            if p == 0:
                await message.channel.send("```cs"+"\n"+"#샌즈!"+"```")
            if p == 1:
                await message.channel.send("```cs"+"\n"+"'샌즈!'"+"```")

client.run(token)
