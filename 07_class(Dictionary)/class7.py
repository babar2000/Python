from typing import Dict, Union, Optional
import pprint # print in beautiful style and function is pprint.pprint(variable name)

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]
# List                      0               1         2
data : Dict[str,str] = {"fname":"Babar Mumtaz",
                        "name":"Zain Babar",
                        "education":"MFIN"}
pprint.pprint(data)
