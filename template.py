import os
from pathlib import Path

project_name = "us_visa"

# here us_visa is not directly mentioned because we are using f string and project_name variable is assigned to us_visa. 
# so that if we change the project name we just need to change the value of project_name variable and rest of the code will work without any change.

list_of_files = [

    f"{project_name}/__init__.py", 
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]



for filepath in list_of_files: 
    ''' for the first iteration filepath will be us_visa/__init__.py and 
    for the second iteration it will be us_visa/components/__init__.py and so on.'''
    filepath = Path(filepath)
    '''
    filepath is representing the individual string element "us_visa/__init__.py" on the list name list_of_files. now string is converted to a path object for the line "filepath = Path(filepath)".
    '''
    filedir, filename = os.path.split(filepath) #filedir will be "us_visa" and filename will be "__init__.py"
    if filedir != "": 
        '''if we does not provide this statement then in that case if we have a file in current directory not inside any directory (example "app.py" not                   "us_visa/app.py" then filedir will be "" and os.makedir("") will s=throw an error.)'''
        os.makedirs(filedir, exist_ok=True)
        ''' 
        without exist_ok = true, suppose you run os.makedirs("us_visa/components") python will see that folder already exists hence it will throw error
        FileExistsError: [Errno 17] File exists: 'us_visa'.
        If exist_ok=True were absent:
        first iteration → folder created successfully
        second iteration → ERROR because folder already exists
        
        after the first iteration us_visa/ folder is created, then If us_visa/ already exists, why does Python create components/ inside it instead of creating
        another separate us_visa/ folder?
        
        after the first iteration when code comes to the line: os.makedirs("us_visa/components", exist_ok = true) it will breakdown path as
        parent folder → us_visa
        child folder  → components
        So Python thinks:
        Does us_visa exist?
        YES
        Does components exist inside us_visa?
        NO
        Create only components
        if the second path has "ind_visa/components/" folder will it create a separate one or will create inside "us_visa/"?
        case1: "os_visa/components"
        result:
        us_visa/
          components/
        case2: "ind_visa/components"
        result:
        ind_visa/
           components/
        case3: "us_visa/ind_visa/components"
        result:
        us_visa/
        ind_visa/
        components/
        '''

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        '''
        not os.path.exists(filepath): The file does not exist at the specified path. 
        os.path.getsize(filepath) == 0: The file exists but has a size of 0  bytes (it is empty).
        
        why not use filename instead of filepath?
        
        because filename contains ONLY the file name. It does NOT contain the folder location. suppose we do open(filename, "w") this becomes  
        open("__init__.py", "w"), then Python creates the file in the CURRENT directory. NOT inside us_visa/. so we use filepath which results in 
        open("us_visa/__init__.py", "w"). Now the file is created INSIDE the folder.
        
        what is the use of the condition "if path.os.path.getsize(filepath) == 0" simply we could have checked The file does not exist at the specified path, 
        through "if not os.path.exists(filepath)" statement ?
        
        In bigger scripts, you may later add:
        
        f.write("some starter code")
        
        In OUR code specifically, since you only do:
        pass
        the size check is mostly unnecessary. This simpler version would behave almost identically:
        if not os.path.exists(filepath):
        with open(filepath, "w"):
        pass

        but how it has worked we can uderstand in following example:

        fisrt time when i ran this code, it executes successfully and all files got created. now in app.py file i wrote print("hello world")
        so in next time when i ran the code else block got executed and got this message: file is already present at: app.py. so basically it will run 
        successfully when it will see folders are empty. otherwise it will print file is already present at: {filepath}.
        
        '''
        
        with open(filepath, "w") as f:
            pass
            '''
            Opening in "w" mode automatically creates the file.
            without with keyword we have to write it in following way:

            f = open(filepath, "w")
            f.close()

            But if an error occurs before close():

            This can cause:

            memory leaks
            file corruption
            locked files

            Internally it behaves like

            f = open(filepath, "w")

            try:
               pass
            finally:
               f.close()

            f is an object of open().

            now if Opening in "w" mode automatically creates the file, then what is use of pass?

            Because Python syntax requires some statement inside the block. because after : Python expects a block, we write pass means:
            "Do nothing." It is a placeholder statement.

            Open file
            Do nothing
            Close file
            '''
    else:
        print(f"file is already present at: {filepath}")