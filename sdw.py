from cryptography.fernet import Fernet, InvalidToken
import os
import atexit
import signal
key = input("Input the key: ") # Use one of the methods to get a key (it must be the same as used in encrypting)
os.system("clear")
input_file = 'encrypted_roster'
output_file = 'roster'

def cleanup():
    os.remove("roster")

# Run cleanup if the terminal session disconnects
def killhandler(signum, frame):
    cleanup()

signal.signal(signal.SIGHUP, killhandler)

def exit_handler():
    cleanup()
    print("\nRoster file cleanup was successful\n")
atexit.register(exit_handler)

# This section defines the function that decrypts the file
def decryptroster():
    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file

        # Note: You can delete input_file here if you want
    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")


# This section defines the saltshell function which serves as a "front end" for salt-ssh
def saltshell():
    print("*" * 59)
    print("\nType in the target pfSenses\n  -These can be seperated by |\n  -You can use * for wildcard\n  -Perl Compatible Regular Expression (PCRE) is supported\n\nExamples:\n  -To target all pfSenses enter UK*\n  -To target all SouthEast pfSenses enter *SouthEast\n")
    print("*" * 59)
    pftarget = input("\n\n\nTarget(s): ")

    if pftarget[0] == '*':
        pfcmd = input("Type in the salt command: ")
        pipe = input("Type a pipe or redirect command. Leave blank for none: ")
        cont = input("\n\nCommand to be run:\n\n          salt-ssh '" + pftarget + "' "+ pfcmd + " " + pipe + "\n\nContinue? y/n: ")
        if cont[0] == 'y':
            decryptroster()
            os.system("salt-ssh '" + pftarget + "' "+ pfcmd +" " + pipe)
            return
        if cont[0] == 'n':
            return
        else:
            os.system("clear")
            print("\n\n\nWhat are you trying to achieve?\n\n\n\n")
            return
    else:
        pfcmd = input("Type in the salt command: ")
        pipe = input("Type a pipe or redirect command. Leave blank for none: ")
        cont = input("\n\nCommand to be run:\n\n          salt-ssh -E '" + pftarget + "' "+ pfcmd + " " + pipe +"\n\nContinue? y/n: ")
        if cont[0] == 'y':
           decryptroster()
           os.system("salt-ssh -E '" + pftarget + "' "+ pfcmd +" " + pipe)
           return
        if cont[0] == 'n':
           return
        else:
            os.system("clear")
            print("\n\n\nWhat are you trying to achieve?\n\n\n\n")
            return


# Run the saltshell function defined above
saltshell()
