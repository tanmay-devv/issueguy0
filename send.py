from pushbullet import Pushbullet as pb
API_KEY=""

file = "send.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = pb(API_KEY)
push = pb.push_note('Please reminder', text)
