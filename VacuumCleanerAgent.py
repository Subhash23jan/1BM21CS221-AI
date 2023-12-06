def vacuum_world():
        # initializing goal_state
        # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}

    location_input = input("Enter Location of Vacuum") #user_input of location vacuum is placed
    status_input = input("Enter status of " + location_input) #user_input if location is dirty or clean
    status_input_complement = input("Enter status of other room")

    print("Initial Location Condition" + str(goal_state))
    next='B'
    if location_input=='B':
        next='A'
    startClean(location_input,next,status_input,status_input_complement,goal_state,0)

def startClean(initial,next,initialState,nextState,goal_state,cost):
    goal_state[initial]='1'
    if initialState=='1':
        cost+=1
        print("Cleaning " +str(initial))
        print("Location Condition" + str(goal_state))
        print("Total cost : " + str(cost))
    else:
        print("No Dust Here " + str(next))
        cost+=1
        print("cost after move : " + str(cost))
    if next=='No':
        print("Location Condition" + str(goal_state))
        print("Total cost : " + str(cost))
    else:
        return startClean(next,'No',nextState,'No',goal_state,cost+1)
    


vacuum_world()
