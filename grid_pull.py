def grid_pull(host,user,port,localpath,hostpath,filename,convert,option='import'):
    """
        Parameters
        ----------
        host : string
            SAS Host Server
        user: string
            Windows USER name e.g JohnDoe
        port : numeric
            port for the server e.g 22
        localpath: string
            Location where the sas file will be saved
        hostpath : string
            Location where the sas file is located in the SAS server
        filename: string
            file name
        convert: numric
            Default set to 1. Converts the sas7bdat file to a Panda Dataframe.
        option: string
            Default set to import. Choose to 'import' from the sas server or 'export' to the sas server
            
    """
        
    try:
        import paramiko
        import getpass
        import os
        import pandas as pd
        #from sas7bdat import SAS7BDAT
        import keyring
        
        #grab user input password
        #p = getpass.getpass(prompt="SAS Grid Password:")
        p=keyring.get_password("SAS",user)
            #create connection to the SASserver
        ssh_client =paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=host,port=port,username=user,password=p)
        
        
        #Change WD
        os.chdir(localpath)
        
        #copy files to local dir
        ftp_client=ssh_client.open_sftp()
        if option=='import':
            ftp_client.get(hostpath+"/"+filename.lower(),filename)
        elif option=='export':
            ftp_client.put(filename,hostpath+"/"+filename.lower())
        #close connection
        ftp_client.close()
        ssh_client.close()
        #convert SAS File
        if convert==1:
            sasdf=pd.read_sas(filename)
            return sasdf
        elif convert==0:
            print("File will not be converted to a PD Dataframe")
    except BaseException as e:
        print("Failed to Authenticate: Check that your hostname,port, Usercode, filename, and Password is correct")