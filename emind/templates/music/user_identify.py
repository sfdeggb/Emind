import random 

def get_indetify_id(description=""):
    #TODO:根据用户的描述信息，返回用户的id
    #从1-100中随机选择一个数作为用户的id
    return random.randint(1,100)

if __name__ =="__main__":
    print(get_indetify_id())