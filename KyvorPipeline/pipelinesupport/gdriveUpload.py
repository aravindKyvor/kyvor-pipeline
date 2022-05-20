import os

def uploadProject(projectFolder, driveFolder):

    if driveFolder == "CanlyTx":
        folderID = "1C9aF5sgrdKJkOm7Xtoqei9NZ32g5GHaF"
    elif driveFolder == "Raw":
        folderID = "1y-tZjhPJBJetP_7O1lmF0_LZlGg1OuqK"
    else:
        folderID = ""

    print("Helo")

    """
        try:
        print("Hello")
        os.environ['GOPATH'] = "/root/go"
        gdrivePath = '$GOPATH/bin/gdrive'
    except:
        gdrivePath = '/root/go/bin/gdrive'
    """

    gdrivePath = '/root/go/bin/gdrive'

    print(gdrivePath)
    #Upload Files
    upload_command = gdrivePath +" upload "+str(projectFolder) + " --recursive "
    print(upload_command)
    if folderID != "":
        upload_command = upload_command + str(" -p ") +str(folderID)
    print(upload_command)
    upload_files = os.popen(upload_command)
    upload_input = upload_files.read()
    print(upload_input)

    return "blahhh"



