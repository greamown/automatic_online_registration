from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time, sys, argparse
from datetime import datetime
import subprocess, sys
from common.operate_lib import first_step, two_step, final_step

def main(args):
    clear = "cls" if sys.platform == "win32" else "clear"
    while True:
        today_now = datetime.now()
        print ("Current date and time = %s" % today_now)
        time.sleep(1)
        subprocess.run(clear, shell=True)
        today_at = today_now.replace(hour=int(args.hour), minute=int(args.minute), second=0)
        if today_now == today_at:
            start_time = time.time()
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://npm.cpami.gov.tw/apply_2_1.aspx")
            first_step(driver, args.email, args.id)
            two_step(driver)
            final_step(driver)
            print("Cost time:",time.time() - start_time)
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--email', help = "The email of Login")
    parser.add_argument('-i', '--id', help= "The ID number of Login")
    parser.add_argument('-hour', '--hour', help = 'Automatic login time- hour')
    parser.add_argument('-min', '--minute', help = 'Automatic login time- minute')
    args = parser.parse_args()
    sys.exit(main(args) or 0)