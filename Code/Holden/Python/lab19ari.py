import requests
import re
import math
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
mr_list = ['mr.','ms.','mrs.','a.d.','b.c.']
while True:
    url = input("Please input link to the .txt file: ")
    response = requests.get(url)
    if response.status_code == 404:
        print("404 ERROR")
        continue
    break
text = (response.text).lower()
wordcount = len(re.findall(r'\w+\'*\w*', text))
cleantext = text
for word in mr_list:
    cleantext = cleantext.replace(word, "d")
sentencecount = len(re.findall(r'\w+[\.\?!]', cleantext))


ariscore = 4.7*(len(text)/wordcount) + 0.5*(wordcount/sentencecount)-21.43
print(ariscore)
if ariscore > 14:
    ariscore =14
ariscore = math.ceil(ariscore)
filename = url.split("/")
filename.reverse()
print(f"The ARI for {filename[0]} is {ariscore} \nThis corresponds to a {ari_scale[ariscore]['grade_level']} level of difficulty \nthat is suitable for an average person {ari_scale[ariscore]['ages']} years old.")
