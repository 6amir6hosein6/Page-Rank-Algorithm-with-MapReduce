import json

links_information = {}
count = 0

url = ""
with open("data-00001") as file:
    for item in file:
        if item != "\n":
            parts = item.split()
            title = parts[0]

            if title == "URL":
                url = parts[1]
                count += 1
                data = {
                    "tokens": {},
                    "mentions": {}
                }
                links_information[url] = data
            else:
                if title == "TOKEN":
                    word = parts[1]
                    word_count = parts[2]
                    links_information[url]["tokens"][word] = word_count
                elif title == "MENTION":
                    link = parts[-1]
                    mention_count = parts[-2]
                    links_information[url]["mentions"][link] = mention_count

jsonFile = open('data-00001.json', 'w')
jsonFile.write(json.dumps(links_information, indent=5))
jsonFile.close()