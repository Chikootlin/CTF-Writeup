For the final we don't need to make the writeup, so thats why ill share the file i use to solve and ill ellaborate how i solve it in a short way.
> I did'nt want to create the writeup because the challenge file is too big, RIP MY LAPTOP

# PT Kucing Empus
So the author gave us a memory file. If i remember correctly, the description of the challenge is, someone give us a malware and the malware send it to their social media account then encrypted all of our files after that. Based on the description, we can filter what social media that can sent a file:
- Instagram
- Facebook
- Twitter/X
- Telegram
- Discord
  
So we can start to analyze it, by using volatility3 and extract all the history to a text, after I filter and try to open all of them I found one suspicioous link that leads to discord server. There you'll find the backup.zip that contain the .xlsx file. And yeah my memory kinda blury on how I got the password but I think it mentioned in one of the file if we try to read the disk using FTK Imager. So thats how I got the flag
