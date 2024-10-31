import requests
import json
import os
import random
from colorama import *
from datetime import datetime, timedelta
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Fabrika:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'api.ffabrika.com',
            'Origin': 'https://ffabrika.com',
            'Pragma': 'no-cache',
            'Referer': 'https://ffabrika.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Fabrika - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def login_telegram(self, query: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/auth/login-telegram'
        data = json.dumps({"webAppData":{"payload":query}})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Web-App-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 201:
                    return result['data']['accessToken']['value']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def profile(self, token: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/profile'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 200:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def scores(self, token: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/scores'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 200:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def claim_daily(self, token: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/daily-rewards/receiving'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })
        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                if response.status_code == 204:
                    return True
                else:
                    return False
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def tap_tap(self, token: str, tap_count: int, retries=3):
        url = 'https://api.ffabrika.com/api/v1/scores'
        data = json.dumps({"count":tap_count})
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 201:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def use_recovery(self, token: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/energies/recovery'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 201:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def tasks(self, token: str, retries=3):
        url = 'https://api.ffabrika.com/api/v1/tasks'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 200:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def tasks_completion(self, token: str, task_id: int, retries=3):
        url = f'https://api.ffabrika.com/api/v1/tasks/completion/{task_id}'
        self.headers.update({
            'Content-Type': 'application/json',
            'Cookie': f"acc_uid={token}"
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['statusCode'] == 201:
                    return result['data']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def process_query(self, query: str):

        token = self.login_telegram(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Token{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if token:
            user = self.profile(token)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['score']['total']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['dailyReward']['daysCount']} Day {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                daily_login = user['dailyReward']['isRewarded']
                if not daily_login:
                    claim = self.claim_daily(token)
                    if claim:       
                        balance = self.scores(token)
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {balance['total']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    balance = self.scores(token)
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                energy_count = user['energy']['balance']
                # count = 250
                count = random.randint(25, 50)
                while energy_count > count:
                    tap_tap = self.tap_tap(token, count)
                    if tap_tap:
                        energy_count -= count
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {tap_tap['score']['total']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Energy{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {energy_count} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                    time.sleep(1)

                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Stopped, {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}No Enough Energy{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                )
                time.sleep(1)

                recovery = user['energy']['currentRecoveryLimit']             
                if recovery > 0:
                    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
                    last_recover = user['energy']['lastRecoveryAt']
                    if last_recover:
                        last_recover_utc = datetime.strptime(last_recover, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc) + timedelta(hours=1)
                    else:
                        last_recover_utc = now_utc

                    last_recover_wib = last_recover_utc.astimezone(wib).strftime('%x %X %Z')
                    
                    if now_utc >= last_recover_utc:
                        use_recover = self.use_recovery(token)
                        if use_recover:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Recovery{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Was Used Successfully {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Recovery{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Failed to Use {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)

                        energy_count = user['energy']['balance']
                        # count = 250
                        count = random.randint(25, 50)
                        while energy_count > count:
                            tap_tap = self.tap_tap(token, count)
                            if tap_tap:
                                energy_count -= count
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {tap_tap['score']['total']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Energy{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {energy_count} Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            time.sleep(1)

                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Stopped, {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}No Enough Energy{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                        time.sleep(1)

                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Recovery{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Already in Use {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Use at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {last_recover_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Recovery{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Empty {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                tasks = self.tasks(token)
                if tasks:
                    for task in tasks:
                        task_id = str(task['id'])

                        if task and not task['isCompleted']:
                            completed = self.tasks_completion(token, task_id)
                            if completed:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['description']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['reward']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['description']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
        
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 60
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Fabrika - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = Fabrika()
    bot.main()