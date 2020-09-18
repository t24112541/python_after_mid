class dt:
    def __init__(self):
        self.dt_name=['a','b','c','d']
        self.dt_tel=[11,22,33,44]
    def add(self,target,data):
        if target=="dt_tel":
            for tel in self.dt_tel:
                if tel==data:
                    return tel!=data
            self.dt_tel.append(data)
        else:
            self.dt_name.append(data)
        return True
        
                
    def get_dt_name(self):
        return self.dt_name
    def get_dt_tel(self):
        return self.dt_tel


def main():
    print("data")
    d=dt()
    stg_1=d.add("dt_tel",22)
    print(stg_1)
    stg_2=d.add("dt_tel",123)
    print(stg_2)
    stg_3=d.add("dt_tel",55)
    print(stg_3)
    stg_3=d.add("dt_name","ola")
    print(stg_3)
    
if __name__=='__main__':
    main()
