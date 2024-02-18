from pushbullet import Pushbullet as pb
API_KEY="o.U9sBZ93Nge27jhquIL3mPensec5DS2Zk"

file = "send.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = pb(API_KEY)
push = pb.push_note('Please reminder', text)
