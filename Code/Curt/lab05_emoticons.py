import random

eyes = [':', 'B', ';', '=', '8', 'X', '>:', 'O:']
nose = ['', '-', 'o', 'c', '^', ]
mouth = [')', ']', '/', 'D', '[', '<', '>', 'O', 'o', 'P', 'p', 'L', 'S', '$', '3', 'J']
emo = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
print(emo)
input("\nPress ENTER to Continue")

#Generate 5
print("\nNow watch me print 5!")
input()

x = 0
while x < 5:
    emo = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    print(emo)
    x += 1
input("\nPress ENTER to Continue")

#Horizontal emoticons

lt_e = ["┌∩┐","╭∩╮","¯\\_","(ง","༼ つ ","(づ","┬┴┬┴┤ ","ヾ","\\ ","ᕙ","ᕦ","☜","╚"]
md_e = ["(◣_◢)","(Ο_Ο)","( * O * )","ô¿ô","( ͡° ͜ʖ ͡°)","(ツ)","ʕ•ᴥ•ʔ","ಠ_ಠ","◕_◕","｡◕‿‿◕｡","(ಥ﹏ಥ)","(⌐■_■)","◉_◉","(•◡•)","(⇀‸↼‶)","(ò_óˇ)","⚆ _ ⚆","ಥ_ಥ","(˚▽˚)","(°ロ°)","( ಠ ͜ʖರೃ)","(ಠ_ಠ)"]
rt_e = ["┌∩┐","╭∩╮","_/¯",")ง"," ༽つ",")づ"," ├┬┴┬┴","ノ♪"," /","ᕗ","ᕤ","☞","☝","=┐"]

print("\nBonus round!")

while True:
    print(f"\n{random.choice(lt_e)}{random.choice(md_e)}{random.choice(rt_e)}")
    x = input("\nHit ENTER to continue or type 'end' to stop ").lower().strip()
    if x == "end":
        break
