import os
import json
import re

dict = json.load(open('**Enter Dictionary PATH Here**', encoding='utf-8'))
dire = "**Enter Directory PATH Here**"
max_duplicate_count = 100 # define the maximum number of duplicate name files

for filename in os.listdir(dire):
    try:
		# define curr and new file name
        curr_name = os.path.join(dire, filename)
        new_name = os.path.join(dire, dict[filename])
        for i in range(max_duplicate_count):
            try:
                os.rename(curr_name, new_name)
            except Exception as e:
				# if new name already exists, try adding a number to the end
                new_name = os.path.join(dire, re.sub('[0-9]*\.', str(i) + '.', dict[filename]))
                continue
            break
    except Exception as e:
        print(e)
