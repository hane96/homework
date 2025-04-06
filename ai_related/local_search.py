import json
import os
import sys
import graderUtil
import random

# a dict stores the final result
task_result = {
    "ini_cost": -1,
    "best_cost": -1,
    "locations": []
} 

#######################################################################
# read task file content
task_file = sys.argv[1]
task_content = graderUtil.load_task_file(task_file)

def count_cost( numplay,numbath,playx,playy,bathx,bathy):
    cost=0
    cost_temp=0
    
    for i in range(numplay): #cost是全部總和 cost_temp是單一個playgrond到bathroom
        cost_temp=999999
        for j in range(numbath):
            cost_temp2=abs(bathx[j]-playx[i])+abs(bathy[j]-playy[i])
            if cost_temp2<cost_temp:
                cost_temp=cost_temp2
        cost=cost+cost_temp

    return cost

if task_content:
    #print(task_content)
# BEGIN_YOUR_CODE
    
    lines = task_content
    if len(lines)<5:
        lines.append(10000)
    #task 2和3用60次的隨機起點
    if lines[0] == '0': #一般的hill climbing search
        park=lines[1].split(',')
        park_x = int(park[0])
        park_y = int(park[1]) #檢查過了
        thirdline=lines[2].split('|')
        playground=int(thirdline[0])
        playground_xy=[]
        playground_x=[]
        playground_y=[]
        score_map=[[0]*playground for i in range(playground)] #scoremap用來記錄cost playground的話用99999表示
        for i in range(playground):
            playground_xy.append(thirdline[i+1])
            xy=playground_xy[i].split(',')
            playground_x.append(int(xy[0]) )
            playground_y.append(int(xy[1]) )#用playground_x[i]和playground_y[i]去存第i個playground的座標
            score_map[playground_x[i]][playground_y[i]]=99999 #playground處cost=99999
        #處理預設廁所
        fourthline=lines[3].split('|')
        initial_bathroom=int(fourthline[0])
        bathroom_xy=[]
        bathroom_x=[]
        bathroom_y=[]

        for i in range(initial_bathroom):
            bathroom_xy.append(fourthline[i+1])
            xy2=bathroom_xy[i].split(',')
            bathroom_x.append(int(xy2[0]) )
            bathroom_y.append(int(xy2[1]) )#用bathroom_x[i]和bathroom_y[i]去存第i個bathroom的座標
            score_map[bathroom_x[i]][bathroom_y[i]]=0 #bathroom處cost=99997
        ##
        inicost=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_x,bathroom_y)#inicost正確了
        task_result["ini_cost"] = inicost
        #開始算best cost
        bestcost=inicost
        min=0
        while(min==0):
            i=0
            for i in range(initial_bathroom):
                if bathroom_y[i]-1>=0 and score_map[bathroom_x[i]][bathroom_y[i]-1]<99997:#測試y-1方向
                    bathroom_ytemp=bathroom_y
                    bathroom_ytemp[i]=bathroom_y[i]-1
                    cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_x,bathroom_ytemp)
                    if cost_temp<bestcost: #更新出更好的y
                        bathroom_y=bathroom_ytemp
                        bestcost=cost_temp
                        break
                    else :
                        bathroom_ytemp[i]=bathroom_ytemp[i]+1
                
                if bathroom_x[i]-1>=0 and score_map[bathroom_x[i]-1][bathroom_y[i]]<99997:#測試x-1方向
                    bathroom_xtemp=bathroom_x
                    bathroom_xtemp[i]=bathroom_x[i]-1
                    cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_xtemp,bathroom_y)
                    if cost_temp<bestcost: #更新出更好的x
                        bathroom_x=bathroom_xtemp
                        bestcost=cost_temp
                        break
                    else :
                        bathroom_xtemp[i]=bathroom_xtemp[i]+1

                if bathroom_y[i]+1<park_y and score_map[bathroom_x[i]][bathroom_y[i]+1]<99997:#測試y+1方向
                    bathroom_ytemp=bathroom_y
                    bathroom_ytemp[i]=bathroom_y[i]+1
                    cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_x,bathroom_ytemp)
                    if cost_temp<bestcost: #更新出更好的y
                        bathroom_y=bathroom_ytemp
                        bestcost=cost_temp
                        break
                    else :
                        bathroom_ytemp[i]=bathroom_ytemp[i]-1

                if bathroom_x[i]+1<park_x and score_map[bathroom_x[i]+1][bathroom_y[i]]<99997:#測試x+1方向
                    bathroom_xtemp=bathroom_x
                    bathroom_xtemp[i]=bathroom_x[i]+1
                    cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_xtemp,bathroom_y)
                    if cost_temp<bestcost: #更新出更好的y
                        bathroom_x=bathroom_xtemp
                        bestcost=cost_temp
                        break
                    else :
                        bathroom_xtemp[i]=bathroom_xtemp[i]-1

                if i==initial_bathroom-1:
                    min=1
        merge_bathroom=[ [x,y] for x,y in zip(bathroom_x,bathroom_y) ]         
        task_result["best_cost"] = bestcost
        task_result["locations"] = merge_bathroom    
        #bestcost 計算結束


        #random hill climbing
    else:
        park=lines[1].split(',')
        park_x = int(park[0])
        park_y = int(park[1]) #檢查過了
        thirdline=lines[2].split('|')
        playground=int(thirdline[0])
        playground_xy=[]
        playground_x=[]
        playground_y=[]
        score_map=[[0]*playground for i in range(playground)] #scoremap用來記錄cost playground的話用99999表示
        for i in range(playground):
            playground_xy.append(thirdline[i+1])
            xy=playground_xy[i].split(',')
            playground_x.append(int(xy[0]) )
            playground_y.append(int(xy[1]) )#用playground_x[i]和playground_y[i]去存第i個playground的座標
            score_map[playground_x[i]][playground_y[i]]=99999 #playground處cost=99999
        #處理預設廁所
        fourthline=lines[3]
        initial_bathroom=int(fourthline)
        randomtime=int(lines[4])
        finalcost=99999
        finalx=[]
        finaly=[]
        finalcost=99999
        bestcost=99999
        
        specialx=[]
        specialy=[]
        for k in range(randomtime):

            bathroom_xy=[]
            bathroom_x=[]
            bathroom_y=[]
            i=0
            for i in range(initial_bathroom): #產生一組bathroom
                check=0
                while check==0:
                    x=random.randint(0,park_x-1)
                    y=random.randint(0,park_y-1)
                    if score_map[x][y]<99997:
                        bathroom_x.append(x)
                        bathroom_y.append(y)
                        check=1
                        break


                
            ##
            
            #開始算best cost
            min=0
            while(min==0):
                i=0
                
                for i in range(initial_bathroom):
                    if bathroom_y[i]-1>=0 and score_map[bathroom_x[i]][bathroom_y[i]-1]<99997:#測試y-1方向
                        bathroom_ytemp=bathroom_y
                        bathroom_ytemp[i]=bathroom_y[i]-1
                        cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_x,bathroom_ytemp)
                        if cost_temp<bestcost: #更新出更好的y
                            bathroom_y=bathroom_ytemp
                            bestcost=cost_temp
                            specialx=bathroom_x.copy()
                            specialy=bathroom_y.copy()
                            break
                        else :
                            bathroom_ytemp[i]=bathroom_ytemp[i]+1
                
                    if bathroom_x[i]-1>=0 and score_map[bathroom_x[i]-1][bathroom_y[i]]<99997:#測試x-1方向
                        bathroom_xtemp=bathroom_x
                        bathroom_xtemp[i]=bathroom_x[i]-1
                        cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_xtemp,bathroom_y)
                        if cost_temp<bestcost: #更新出更好的x
                            bathroom_x=bathroom_xtemp
                            bestcost=cost_temp
                            specialx=bathroom_x.copy()
                            specialy=bathroom_y.copy()
                            break
                        else :
                            bathroom_xtemp[i]=bathroom_xtemp[i]+1

                    if bathroom_y[i]+1<park_y and score_map[bathroom_x[i]][bathroom_y[i]+1]<99997:#測試y+1方向
                        bathroom_ytemp=bathroom_y
                        bathroom_ytemp[i]=bathroom_y[i]+1
                        cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_x,bathroom_ytemp)
                        if cost_temp<bestcost: #更新出更好的y
                            bathroom_y=bathroom_ytemp
                            bestcost=cost_temp
                            specialx=bathroom_x.copy()
                            specialy=bathroom_y.copy()
                            break
                        else :
                            bathroom_ytemp[i]=bathroom_ytemp[i]-1

                    if bathroom_x[i]+1<park_x and score_map[bathroom_x[i]+1][bathroom_y[i]]<99997:#測試x+1方向
                        bathroom_xtemp=bathroom_x
                        bathroom_xtemp[i]=bathroom_x[i]+1
                        cost_temp=count_cost(playground,initial_bathroom,playground_x,playground_y,bathroom_xtemp,bathroom_y)
                        if cost_temp<bestcost: #更新出更好的x
                            bathroom_x=bathroom_xtemp
                            bestcost=cost_temp
                            specialx=bathroom_xtemp.copy()
                            specialy=bathroom_y.copy()
                            break
                        else :
                            bathroom_xtemp[i]=bathroom_xtemp[i]-1

                    if i==initial_bathroom-1:
                        min=1
                if finalcost>bestcost:
                    finalcost=bestcost
                    finalx=specialx.copy()
                    finaly=specialy.copy() #這裡出問題應該要確保copy的關係

        merge_bathroom=[ [x,y] for x,y in zip(finalx,finaly) ]         
        task_result["ini_cost"]=bestcost
        
            #bestcost 計算結束
        task_result["best_cost"] = finalcost
        task_result["locations"] = merge_bathroom


#task_result["ini_cost"] = 15
#task_result["best_cost"] = 9
#task_result["locations"] = [[1,2]]

#task_result["best_cost"] = 7
#task_result["locations"] = [[2,1]]


#task_result["ini_cost"] = 9
#task_result["best_cost"] = 7
#task_result["locations"] = [[0,1],[1,2]]
#




# END_YOUR_CODE
#######################################################################

# output your final result
print(json.dumps(task_result))