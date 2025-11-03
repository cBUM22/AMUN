import osintF
import am
import bf
import kl
import ps
import sms
import vs
import wc
import help

tag = r"""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\____\                /::\____\        
       /::::\    \              /::::|   |               /:::/    /               /::::|   |        
      /::::::\    \            /:::::|   |              /:::/    /               /:::::|   |        
     /:::/\:::\    \          /::::::|   |             /:::/    /               /::::::|   |        
    /:::/__\:::\    \        /:::/|::|   |            /:::/    /               /:::/|::|   |        
   /::::\   \:::\    \      /:::/ |::|   |           /:::/    /               /:::/ |::|   |        
  /::::::\   \:::\    \    /:::/  |::|___|______    /:::/    /      _____    /:::/  |::|   | _____  
 /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/____/      /\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\|:::|    /      /::\____\/:: /    |::|   /::\____\
\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /|:::|____\     /:::/    /\::/    /|::|  /:::/    /
 \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\    \   /:::/    /  \/____/ |::| /:::/    / 
          \::::::/    /               /:::/    /    \:::\    \ /:::/    /           |::|/:::/    /  
           \::::/    /               /:::/    /      \:::\    /:::/    /            |::::::/    /   
           /:::/    /               /:::/    /        \:::\__/:::/    /             |:::::/    /    
          /:::/    /               /:::/    /          \::::::::/    /              |::::/    /     
         /:::/    /               /:::/    /            \::::::/    /               /:::/    /      
        /:::/    /               /:::/    /              \::::/    /               /:::/    /       
        \::/    /                \::/    /                \::/____/                \::/    /        
         \/____/                  \/____/                  ~~                       \/____/         
                                                                                                    
                                (The hidden one - Invisible creator)
                                                                                                    By: cBUM22
                                                                                                    v: 1.0.0
                                                                                                                                
"""

options = r"""
-pS : port scanner      -osint : discover public DNS footprint
-bF: brute force        -vS : vulnerability scanner on websites
-wC : web crawler       -kL : key logger
-aM : mail sending      -sms : sms message sending
-mIP : mask IP address
           
-help : read more purpose of the otions
-croom : create fully encrypted chat rooms on specific ports with passwords
-droom : delete specific room with port number and password
-jroom : join a specific room with port number and password
"""

def check_user_tool():
    print(f"\033[31m{tag}","\n")
    print(f"\033[33mSELECT AN OPTION:\n",f"\033[35m{options}")

    user_input = input("\033[32m: ")

    if user_input == "-osint":
        target_domain = input("\033[31mTarget domain: ")
        osintF.get_target_domain(target_domain)
    elif user_input == "-pS":
        pass
    elif user_input == "-help":
        print(help.helpTable)
    else:
        check_operation = input(f"\033[31mNo option such as {user_input} type '-help' for more information\n: ")
        check_user_tool(check_operation)

if __name__=="__main__":
    check_user_tool()