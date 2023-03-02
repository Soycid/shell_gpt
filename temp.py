import json
import os 

my_favorite_animal = json.loads(os.popen("python /Users/alpercanberk/Projects/shell_gpt/sgpt.py -r \"my favorite animal\"").read())[0]
animal_link = os.popen(f"python /Users/alpercanberk/Projects/shell_gpt/sgpt.py \"give me the wikipedia link for {my_favorite_animal}: \" ").read()
print(animal_link)