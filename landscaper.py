##Game state variables

game = {"tool":0, "money": 0}

tools = [
    {"name": "teeth", "cost": 0, "profit": 1},
    {"name": "rusty scissors", "cost": 5, "profit": 5},
    {"name": "pushy lawnmower", "cost": 25, "profit": 50},
    {"name": "battery powered lawnmower", "cost": 250, "profit": 100},
    {"name": "students", "cost": 500, "profit": 250},
]


#Game option function
def cut_grass():
    tool = tools[game["tool"]]
    print(f"You cut grass with your{tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]
    
def check_status():
    tool = tools[game["tool"]]
    money = game["money"]
    print(f"You have the tool, {tool['name']} and have money of {money}")
    
def upgrade():
    if (game["tool"] >= len(tools) - 1):
        print("no more tools")
    
    next_tool = tools[game['tool'] + 1]
    if (next_tool == None):
        print("There is no more tools")
        return 0
    if (game['money'] < next_tool['cost']):
        print("Not enough money to buy the tool")
        return 0
    print("you have upgraded your tool")
    game ["money"] -= next_tool["cost"]
    game ["tool"] += 1
    
def win_check():
    if(game["tool"] == 4 and game["money"] >= 1000):
        print("You've won!")
        return True
    return False

while (True) :
    i = input("[1] Cut grass [2] Check tool and money [3] Upgrade tool [4] Quit")
    i = int(i)
    if(i == 1):
        cut_grass()
        
    if(i == 2):
        check_status()
    
    if(i == 3):
        upgrade()
    
    if(i == 4):
        print("you quit the game!")
        break
    
    if(win_check()):
        break