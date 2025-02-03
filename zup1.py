import os
import shutil
import subprocess 

logo = (f''' \033[1;32m  

                        WALANG LOGO EH
                                                  
''')

red = "\033[1;31m"    # Bold red
c = "\033[1;96m"      # Cyan (for overview heading)
g = "\033[1;32m"      # Bold green
r = "\033[0m"         # Reset color
wh = "\033[1;37m"     # Bold white

def clear_screen():
    os.system('clear')

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0 

def overview():
    print(logo) 
    print(f"\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━[{g}OVERVIEW{g}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    total_accounts = count_lines("/sdcard/Test/toka.txt")
    total_pages = count_lines("/sdcard/Test/tokp.txt")
    print(f"  {g}                   TOTAL ACCOUNTS: {g}{total_accounts}{g}")
    print(f'{g} ════════════════════════════════════════════════════════════════{r}')

def git_pull_repository():
    repo_path = '.'
    try:
        print(f"{c}Updating the repository...{r}")
        subprocess.run(['git', 'pull'], cwd=repo_path, check=True)
        print(f"{wh}Repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the repository: {e}{r}")

def clone_and_run(repo_url, script_name):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    if not os.path.exists(repo_name):
        os.system(f'git clone {repo_url}')
    
    os.chdir(repo_name)
    os.system(f'python {script_name}')
    os.chdir('..')

def main_menu():
    clear_screen()
    overview()  # Call the overview function here

    print("[1] EXTRACT ACCOUNT")
    print("[2] AUTO REACTS FOR POST/PHOTO/GROUP POSTS")
    print("[3] AUTO REACTS FOR VID")
    print("[4] AUTO REACTS FOR REELS")
    print("[5] SPAM SHARES")
    print("[C] AUTO REMOVE DEAD ACCOUNTS")
    print("[RDP] REMOVE DUPLICATE ACCOUNTS")
    print("[R] Reset")
    print("[E] Exit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == '1':
        extract_account()
    elif choice == '2':
        bundle_reacts()
    elif choice == '3':
        auto_working_vid()
    elif choice == '4':
        auto_reacts_reels()
    elif choice == '5':
        spam_share()
    elif choice == 'C':
        acc_checker()
    elif choice == 'RDP':
        dupli_remover()
    elif choice == 'R':
        reset()
    elif choice == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()
              
def extract_account():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'updated-acc-extractor.py'
    clone_and_run(repo_url, script_name)

def bundle_reacts():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'bundle_reacts.py'
    clone_and_run(repo_url, script_name)

def auto_working_vid():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'working-vid.py'
    clone_and_run(repo_url, script_name)

def auto_reacts_reels():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'reels_reacts.py'
    clone_and_run(repo_url, script_name)

def spam_share():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'spam_share.py'
    clone_and_run(repo_url, script_name)

def acc_checker():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'acc_checker.py'
    clone_and_run(repo_url, script_name)
    
def dupli_remover():
    repo_url = 'https://github.com/TOOLSv1/FB-TOOL'
    script_name = 'dupli_remover.py'
    clone_and_run(repo_url, script_name)

def reset():
    folder_path = '/sdcard/Test'
   
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Successfully deleted the folder: {folder_path}")
        except Exception as e:
            print(f"Error while deleting the folder: {e}")
    else:
        print(f"The folder {folder_path} does not exist.")

if __name__ == "__main__":
    main_menu()