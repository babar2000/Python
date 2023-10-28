from typing import Tuple, Dict
def my_function(a:int,b:int,*abc:Tuple[int,...],**xyz:Dict[str,int])->None:
    print(a,b,abc,xyz)
my_function(1,2,7,8,9,0,3,c=20,d=76,x=765)