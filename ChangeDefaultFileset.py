import os

filename="game.cfg"
directory = os.path.dirname(os.path.realpath(__file__)) + "\\Champions"
lolMap="_SR_CLASSIC"
itemSet="e47e5cd0-58cc-11e9-bcfa-29c22cc0da95"

gameCFG = open(filename, "r")
data=[]#contents of game.cfg
recommendPageIndex=-1
lossOfControlIndex=-1
index=0
defaultItemSetList=[]#defaults to assign to game.cfg
for line in gameCFG:
    if "[RecommendPage]" in line:
        recommendPageIndex=index
        data.append(line)
    elif "[LossOfControl]" in line:
        lossOfControlIndex=index

    if recommendPageIndex==-1 or lossOfControlIndex!=-1:
        data.append(line)
    index += 1



for fileName in os.listdir(directory):
    print(fileName, end=", ")
    assign=fileName+lolMap+"="+itemSet
    defaultItemSetList.append(assign)

for i in range(len(defaultItemSetList)-1,-1,-1):

    data.insert(recommendPageIndex+1,defaultItemSetList[i]+"\n")

gameCFGWrite=open(filename, "w")
for item in data:
    gameCFGWrite.write(item)

    
    
