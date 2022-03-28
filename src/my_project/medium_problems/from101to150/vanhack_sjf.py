def sjf(jobs: list, index: int) -> int:
    
    waiting_time = list()
    
    waiting_time.append(0)
    
    total_time_list = list()
    
    process_list = list()
    
    for i in range(len(jobs)):
        process_list.append({"id":i, "value":jobs[i]})
        
    def sort_list(a):
        return a["value"] 
    
    def calculate_waiting_time(sorted_list, waiting_time):
        for i in range(1,len(sorted_list)):
            waiting_time.append(sorted_list[i-1]['value'] + waiting_time[i-1])
            
    def calculate_time_for_each_task(sorted_list, total_time_list):
        for i in range(len(sorted_list)):
            total_time_list.append({"id":sorted_list[i]["id"], 
                                    "time": sorted_list[i]["value"] + waiting_time[i]})
    
    def find_clock_cycles(total_time_list, index):
        for i in range(len(total_time_list)):
            if total_time_list[i]['id'] == index:
                return total_time_list[i]['time']
        
       
    process_list.sort(key= lambda point: sort_list(point) )
    
    sorted_list = process_list
    
    calculate_waiting_time(sorted_list, waiting_time)
    
    calculate_time_for_each_task(sorted_list, total_time_list)
    
    return find_clock_cycles(total_time_list, index)