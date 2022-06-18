import typing

from points_cell import PointsCell
import random

def get_list_of_points(file_with_rewards):
    list_of_cell_points:typing.List[PointsCell]=[]
    for record in file_with_rewards.readlines():
        if record[0]=="#":
            continue
        fields_list=record.split(" ")
        fields_list=list(filter("".__ne__,fields_list))
        for i,field in enumerate(fields_list):
            fields_list[i]=field.strip("\n")
        list_of_cell_points.append(PointsCell(int(fields_list[0]),int(fields_list[1]),int(fields_list[2]),float(fields_list[3])))
    return list_of_cell_points

def get_left_bondary(x,list_of_cell_points:typing.List[PointsCell]):
    min=None
    for cell in list_of_cell_points:
        if cell.x>x:
            continue
        if min==None:
            min=cell
        elif cell.x>min.x:
            min=cell
    return min
def get_right_bondary(x,list_of_cell_points:typing.List[PointsCell]):
    max=None
    for cell in list_of_cell_points:
        if cell.x<x:
            continue
        if max==None:
            max=cell
        elif cell.x<max.x:
            max=cell
    return max

def sort(x):
    return x[1]

if __name__ == "__main__":
    file=open("rewards.txt")
    rewards=get_list_of_points(file)
    rand=random.Random()
    number_of_iterations=int(input("podaj liczbe iteracji:>"))
    # memory_length=int(input("podaj długość pamięci:>"))
    file.close()
    goals_of_attack=[]
    for i in range(0,number_of_iterations):
        x=rand.randint(0,1040)
        bondariers=[get_right_bondary(x,rewards),get_left_bondary(x,rewards)]
        sum=0
        k=0
        for bond in bondariers:
            if bond!=None:
                k=k+1
                sum=sum+bond.points
        sum=sum/float(k)
        goals_of_attack.append((x,sum))
    res_fil=open("goals_of_attack.csv","w")



    goals_of_attack.sort(key=sort,reverse=True)
    res_fil.write("x;points\n")
    for goal in goals_of_attack:
        res_fil.write("%d;%.2f\n"%(goal[0],goal[1]))

    file.close()
