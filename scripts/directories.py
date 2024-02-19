import os

def create_directory(root_path:str, years:set, months:set)->None:
    dmonths = {
        '01':'january', 
        '02':'february', 
        '03':'march',
        '04':'april', 
        '05':'may', 
        '06':'june', 
        '07':'july', 
        '08':'august', 
        '09':'september', 
        '10':'october', 
        '11':'november', 
        '12':'december'
    }
    if not os.path.exists(root_path):
        os.mkdir(root_path)
    for year in years:
        path = f"{root_path}/{year}"
        if not os.path.exists(path):
            os.mkdir(path)
        for month in months:
            sec_path = path + '/' + dmonths[month]
            if not os.path.exists(sec_path):
                os.mkdir(sec_path)
