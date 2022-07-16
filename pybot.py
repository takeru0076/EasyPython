command_file = open("pybot.txt", encoding="utf-8")
raw_data = command_file.read()
command_file.close()
lines = raw_data.spliitlines()
 
 bot_dict = {}
 for line in lines:
     word_list = line.split(",")
     key = word_list[0]
     responnse = word_list[1]
     bot_dict[key] = response