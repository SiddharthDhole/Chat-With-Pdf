import os 


def save_uploadedfile(uploadedfile,directory = 'pdf'):
    '''Save the uploaded file to the specified directory and return path of it'''
    if uploadedfile is not None : 
        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory,exist_ok=True)
        # Save the file
        with open(os.path.join(directory, uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())  
        path = os.path.join(directory, uploadedfile.name)
        return path  
    


def remove_uploadedfile(directory = 'pdf'):
    ''' Remove uploaded files from pdf directory and remove them from its'''
    for i in os.walk(directory):
                    for file in i[2]:
                        os.remove(os.path.join(i[0], file)) 
    