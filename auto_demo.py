from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time, sys, argparse
from datetime import datetime
import subprocess, sys
from common.operate_lib import first_step, two_step, final_step

def main(args):
    clear = "cls" if sys.platform == "win32" else "clear"
    second = 0
    while True:
        today_now = datetime.now()
        print ("Current date and time = %s" % today_now)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        subprocess.run(clear, shell=True)
        today_at = today_now.replace(hour=int(args.hour), minute=int(args.minute), second=second)
        if today_now == today_at:
            try:
                start_time = time.time()
                driver.get("https://npm.cpami.gov.tw/apply_2_1.aspx")
                first_step(driver, args.email, args.id)
                two_step(driver)
                FINAL = final_step(driver)
                if FINAL:
                    print("Cost time:",time.time() - start_time) 
                    break
            finally:
                second = int(str(datetime.now()).split(":")[-1].split(".")[0]) + 10
                if second > 59:
                    second = 0
                    args.minute = int(args.minute) + 1
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--email', help = "The email of Login")
    parser.add_argument('-i', '--id', help= "The ID number of Login")
    parser.add_argument('-hour', '--hour', help = 'Automatic login time- hour')
    parser.add_argument('-min', '--minute', help = 'Automatic login time- minute')
    args = parser.parse_args()
    sys.exit(main(args) or 0)