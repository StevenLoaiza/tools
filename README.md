# Tools
Misc repo storing functions that are used most often.

## grid_pull.py
The function allows SAS datasets to be copied into a local directories via Python.

![](https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2017/07/symmetric-encryption-ssh-tutorial.jpg)

*Aman L from Hostinger*

Library Dependencies:
Make sure to install via conda
- Paramiko 
- getpass 
- keyring
- pandas
- os

### Set Password:
Run this code first, and it will prompt you to set up your password. Only change the USERNAME to your own.

```python
import keyring
import getpass
keyring.set_password("SAS","USERNAME",getpass.getpass())
```

### Import Function
Set the directoy where grid_pull.py is saved.
```python
import os
os.chdir("/yourlocalfileholdingpyscript")
%run grid_pull
```
### Data Transfer /View
Below is the code to transfer a *.sas7bdat file into a local directory and import it into your jupyter notebook as a pandas dataset.
```python
#Pull data from SAS server
my_df=grid_pull(
    host="hostname",
    user="Username",
    port=portnumber,
    localpath="/Local Path/",
    hostpath="/SAS Server Path/",
    filename="FILENAME.sas7bdat"),
    convert=1,
    option='import'

#First 5 obs
my_df.head(5)
```

