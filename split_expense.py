import numpy as np

def create_dict(keys, values):
    return dict(zip(keys, values))# + [None] * (len(keys) - len(values))))

members = input('Enter distinct name of members separated by space (order matters)\n')
members = members.split(' ')
event_wise_exp = {}
spent_dic = {}
data_consumed_arr = np.array([])
data_spent_arr = np.array([])

def print_essential():
    print('Enter member name then total amount spent by him, then purpose and finally distribution in sequence \n',members)
    print('And enter -1 to calculate!')

print_essential()
iter = 1
while True:
    # Handle the member name should be in member list
    # Add functionality of many people spending on same task
    event = input(f'Event {iter}\n')
    if event=='-1': break
    event = event.split(' ')
    try:
        event_wise_exp[event[-len(members)-1]] = np.array(event[-len(members):],dtype=float)
        spent_dic[event[-len(members)-1]] = np.array(event[:-len(members)-1],dtype=float)
    except: 
        print('List the event in proper format, try again!')
        print_essential()
        continue
    data_consumed_arr = np.append(data_consumed_arr,event_wise_exp[event[-len(members)-1]])
    data_spent_arr = np.append(data_spent_arr,spent_dic[event[-len(members)-1]])
    
    iter+=1

data_consumed_arr = data_consumed_arr.reshape((len(event_wise_exp),int(np.shape(data_consumed_arr)[0]/len(event_wise_exp))))
total_consumed = np.sum(data_consumed_arr,axis=0)
data_spent_arr = data_spent_arr.reshape((len(event_wise_exp),int(np.shape(data_spent_arr)[0]/len(event_wise_exp))))
total_spent = np.sum(data_spent_arr,axis=0)
net = total_spent-total_consumed
print(create_dict(members,net))



    