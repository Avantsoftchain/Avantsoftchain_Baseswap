import asyncio
import json
import logging
import os
import re

from Src.Hamster import HamsterKombatClicker
from Src.utils import RESET, CYAN, LIGHT_YELLOW, YELLOW, LIGHT_MAGENTA, WHITE, LIGHT_CYAN, get_status, LIGHT_BLUE, GREEN, \
    line_before, line_after, save_settings, load_settings


def choose_account(default=True, token_number='HAMSTER_TOKEN_1'):
    if default:
        print(f'Вы вошли используя `{token_number}` по умолчанию')
        return os.getenv('HAMSTER_TOKEN_1')

    accounts = []
    env_vars = {key: os.getenv(key) for key in os.environ if key in os.environ}
    for key, value in env_vars.items():
        if key.startswith('HAMSTER'):
            accounts.append(value)

    if len(accounts) > 1:
        print(f"Обнаружено аккаунтов {len(accounts)}: ")
        account_dict = {}
        for e, token in enumerate(accounts):
            hamster = HamsterKombatClicker(token)
            account_info = hamster.get_account_info()
            username = account_info['username']
            first_name = account_info['firstName']
            last_name = account_info['lastName']
            print(f"[{e + 1}] · {first_name} {last_name} ({username})")
            account_dict[str(e + 1)] = token

        account_choice = input(f"\nКакой аккаунт хотите использовать?\nВыберите номер: ")

        if account_choice in account_dict:
            return account_dict[account_choice]
        else:
            print("Некорректный выбор. Попробуйте снова.")
            return choose_account(default=False)
    else:
        return accounts[0]


# --- CONFIG --- #

HAMSTER_TOKEN = choose_account()
hamster_client = HamsterKombatClicker(HAMSTER_TOKEN)
settings = load_settings()

# --- CONFIG --- #


def generate_promocodes(prefix='', apply_promo=False):
    count = input(f"\nКакое количество промокодов генерировать?\nEnter(по умолчанию 1): ")
    if count == '':
        count = 1
        print("Количество промокодов не указано. Генерируется 1 по умолчанию")

    if int(count) <= 0:
        logging.error(f"\nКоличество должно быть числом больше 0")

    try:
        send_to_group = settings['send_to_group']
        save_to_file = settings['save_to_file']
        spinner = 'shark'
        asyncio.run(hamster_client.get_promocodes(int(count), send_to_group, apply_promo, prefix, save_to_file, spinner))

    except Exception as e:
        logging.error(e)

    finally:
        pass


def main_menu():
    activities = hamster_client._activity_cooldowns()
    for activity in activities:
        if 'taps' in activity:
            taps_status = get_status(activity['taps']['isClaimed'])
            taps_cooldown = activity['taps']['remain']
        if 'tasks' in activity:
            task_status = get_status(activity['tasks']['isClaimed'])
            task_cooldown = activity['tasks']['remain']
        if 'cipher' in activity:
            cipher_status = get_status(activity['cipher']['isClaimed'])
            cipher_cooldown = activity['cipher']['remain']
        if 'combo' in activity:
            combo_status = get_status(activity['combo']['isClaimed'])
            combo_cooldown = activity['combo']['remain']
        if 'minigame' in activity:
            minigame_status = get_status(activity['minigame']['isClaimed'])
            minigame_cooldown = activity['minigame']['remain']
    print()
    memu = (
        f"\nНастройки \n"
        f"  ⚙️  Отправлять в группу:  {get_status(settings['send_to_group'])} (toggle_group · включить/отключить)\n"
        f"  ⚙️  Применять промокоды:  {get_status(settings['apply_promo'])} (toggle_apply · включить/отключить)\n"
        f"  ⚙️  Сохранять в файл:     {get_status(settings['save_to_file'])} (toggle_file  · включить/отключить)\n\n"
        f"Главное меню \n"
        f"  Какую активность хотите выполнить? \n"
        f"  {LIGHT_YELLOW}# |  {RESET}📝 {YELLOW}Информация {WHITE} \n"
        f"  {LIGHT_YELLOW}1 |  {RESET}👆 {YELLOW}Клики {WHITE}       {taps_status} · Осталось: {taps_cooldown}\n"
        f"  {LIGHT_YELLOW}2 |  {RESET}📑 {YELLOW}Задания {WHITE}     {task_status} · Осталось: {task_cooldown} \n"
        f"  {LIGHT_YELLOW}3 |  {RESET}🔍 {YELLOW}Шифр {WHITE}        {cipher_status} · Осталось: {cipher_cooldown} \n"
        f"  {LIGHT_YELLOW}4 |  {RESET}🔑 {YELLOW}Миниигра {WHITE}    {minigame_status} · Осталось: {minigame_cooldown} \n"
        f"  {LIGHT_YELLOW}5 |  {RESET}💰 {YELLOW}Комбо {WHITE}       {combo_status} · Осталось: {combo_cooldown} \n"
        f"  {LIGHT_YELLOW}6 |  {RESET}🎁 {YELLOW}Промокоды {WHITE}    \n"
        f"  {LIGHT_YELLOW}$ |  {RESET}💲 {YELLOW}Список самых выгодных карт {WHITE} \n"
        f"  {LIGHT_YELLOW}+ |  {RESET}⭐️ {YELLOW}Купить карту `+ID_Карты` (напрмиер +dao) {WHITE} \n"
        f"  {LIGHT_YELLOW}m |  {RESET}📝 {YELLOW}Показать меню {WHITE} \n"
        f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW}Выйти{WHITE}"
    )
    print(memu.strip())


def playground_menu():
    promos = hamster_client._get_promos()[0]['promo']

    keys_per_day = 4
    bike = cube = clon = trin = ""
    bike_keys = cube_keys = clon_keys = trin_keys = 0
    bike_cooldown = cube_cooldown = clon_cooldown = trin_cooldown = "n/a"
    bike_status = cube_status = clon_status = trin_status = "n/a"

    for promo in promos:
        if promo['name'] == 'Bike Ride 3D':
            bike = promo['name']
            bike_keys = promo['keys']
            bike_cooldown = promo['remain']
            bike_status = get_status(promo['isClaimed'])
        else:
            bike = 'Bike Ride 3D'

        if promo['name'] == 'Chain Cube 2048':
            cube = promo['name']
            cube_keys = promo['keys']
            cube_cooldown = promo['remain']
            cube_status = get_status(promo['isClaimed'])
        else:
            cube = 'Chain Cube 2048'

        if promo['name'] == 'My Clone Army':
            clon = promo['name']
            clon_keys = promo['keys']
            clon_cooldown = promo['remain']
            clon_status = get_status(promo['isClaimed'])
        else:
            clon = 'My Clone Army'

        if promo['name'] == 'Train Miner':
            trin = promo['name']
            trin_keys = promo['keys']
            trin_cooldown = promo['remain']
            trin_status = get_status(promo['isClaimed'])
        else:
            trin = 'Train Miner'

        if promo['name'] == 'Merge Away':
            mrge = promo['name']
            mrge_keys = promo['keys']
            mrge_cooldown = promo['remain']
            mrge_status = get_status(promo['isClaimed'])
        else:
            mrge = 'Merge Away'

        if promo['name'] == 'Twerk Race':
            twrk = promo['name']
            twrk_keys = promo['keys']
            twrk_cooldown = promo['remain']
            twrk_status = get_status(promo['isClaimed'])
        else:
            twrk = 'Twerk Race'

    max_width = max(len(bike), len(cube), len(clon), len(trin), len(mrge), len(twrk))
    memu = (
        f"\n\n🎮  Игровая площадка \n"
        f"  Для какой игры хотите получить промокоды? \n"
        f"  {LIGHT_YELLOW}1 |  {RESET}🚴 {YELLOW} {LIGHT_YELLOW}{bike:<{max_width}} {WHITE}  {bike_keys}/{keys_per_day}  {bike_status} · Осталось: {bike_cooldown} \n"
        f"  {LIGHT_YELLOW}2 |  {RESET}🎲 {YELLOW} {LIGHT_BLUE}{cube:<{max_width}} {WHITE}  {cube_keys}/{keys_per_day}  {cube_status} · Осталось: {cube_cooldown} \n"
        f"  {LIGHT_YELLOW}3 |  {RESET}🎮 {YELLOW} {LIGHT_MAGENTA}{clon:<{max_width}} {WHITE}  {clon_keys}/{keys_per_day}  {clon_status} · Осталось: {clon_cooldown} \n"
        f"  {LIGHT_YELLOW}4 |  {RESET}🚂 {YELLOW} {LIGHT_CYAN}{trin:<{max_width}} {WHITE}  {trin_keys}/{keys_per_day}  {trin_status} · Осталось: {trin_cooldown} \n"
        f"  {LIGHT_YELLOW}5 |  {RESET}🙍‍ {YELLOW} {GREEN}{mrge:<{max_width}} {WHITE}  {mrge_keys}/{keys_per_day}  {mrge_status} · Осталось: {mrge_cooldown} \n"
        f"  {LIGHT_YELLOW}6 |  {RESET}🏃 {YELLOW} {CYAN}{twrk:<{max_width}} {WHITE}  {twrk_keys}/{keys_per_day}  {twrk_status} · Осталось: {twrk_cooldown} \n"
        f"  {LIGHT_YELLOW}* |  {RESET}🎉 {YELLOW} Для всех игр {WHITE} \n"
        f"  {LIGHT_YELLOW}9 |  {RESET}🔙 {YELLOW} В главное меню {WHITE} \n"
        f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW} Выйти {WHITE} \n"
    )
    print(memu.strip())


def handle_main_menu_choice(choice):
    if choice == '#':
        line_after()
        print(hamster_client.daily_info())

    elif choice == '1':
        line_after()
        hamster_client.complete_taps()

    elif choice == '2':
        line_after()
        hamster_client.complete_daily_tasks()

    elif choice == '3':
        line_after()
        hamster_client.complete_daily_chipher()

    elif choice == '4':
        line_after()
        hamster_client.complete_daily_minigame()

    elif choice == '5':
        line_after()
        upgrades_info = hamster_client._collect_upgrades_info()
        if all(card['available'] for card in upgrades_info['cards']):
            hamster_client.complete_daily_combo()
        else:
            choice = input(f"Сегодня не все карты доступны!\nХотите купить только доступные? Y(да) / Enter(нет): ")
            if str(choice.lower()) == 'y'.lower():
                hamster_client.complete_daily_combo(buy_anyway=True)

    elif choice == '6':
        handle_playground_menu()

    elif choice == '$':
        line_after()
        top_10_cards = hamster_client.evaluate_cards()
        print(f"Топ 20 самых выгодных карт (показаны только доступные для покупки): \n")
        for card in top_10_cards:
            print(
                f"🏷  {LIGHT_YELLOW}{card['name']} · `{card['section']}`{WHITE} ID ({card['id']}) \n"
                f"💰  Стоимость: {YELLOW}{card['price']:,}{WHITE} · +{card['profitPerHour']} в час \n"
                f"⌚️  Окупаемость (в часах):{LIGHT_MAGENTA} {card['payback_period']}{WHITE} \n"
                f"📊  Коэффициент рентабельности:{LIGHT_CYAN} {card['profitability_ratio']:.5f}{WHITE}"
            )
            print("-" * 30)

    elif choice.startswith('+'):
        line_after()
        match = re.search(pattern=r'\+(.*?)$', string=choice)
        if match:
            upgrade_id = match.group(1)
            hamster_client._buy_upgrade(upgradeId=upgrade_id)

    elif choice == 'm':
        line_after()
        main_menu()

    elif choice == '0':
        line_after()
        print("Выход")
        line_before()
        exit(1)

    elif choice == 'toggle_group':
        line_after()
        settings['send_to_group'] = not settings['send_to_group']
        save_settings(settings)
        status = 'включена' if settings['send_to_group'] else 'отключена'
        print(f'Отправка промокодов в группу {status}')
        line_before()
        main_menu()

    elif choice == 'toggle_file':
        line_after()
        settings['save_to_file'] = not settings['save_to_file']
        save_settings(settings)
        status = 'включено' if settings['save_to_file'] else 'отключено'
        print(f'Сохранение в файл {status}')
        line_before()
        main_menu()

    elif choice == 'toggle_apply':
        line_after()
        settings['apply_promo'] = not settings['apply_promo']
        status = 'включено' if settings['apply_promo'] else 'отключено'
        save_settings(settings)
        print(f'Применение промокодов по умолчанию {status}')
        line_before()
        main_menu()

    else:
        line_after()
        print("Такой опции нет")


def handle_playground_menu():
    while True:
        playground_menu()
        choice = input(f"\nВыберите действие\n{CYAN}(1/2/3/4/5/6/*/9/0): {RESET}")
        line_after()

        choice_text = f"Хотите применить промокоды после получения?\nY(да) / Enter(Нет): "

        if choice == '1':
            if settings['apply_promo']:
                generate_promocodes(prefix='BIKE', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='BIKE', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='BIKE')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '2':
            if settings['apply_promo']:
                generate_promocodes(prefix='CUBE', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='CUBE', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='CUBE')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '3':
            if settings['apply_promo']:
                generate_promocodes(prefix='CLONE', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='CLONE', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='CLONE')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '4':
            if settings['apply_promo']:
                generate_promocodes(prefix='TRAIN', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='TRAIN', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='TRAIN')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '5':
            if settings['apply_promo']:
                generate_promocodes(prefix='MERGE', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='MERGE', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='MERGE')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '6':
            if settings['apply_promo']:
                generate_promocodes(prefix='TWERK', apply_promo=settings['apply_promo'])
            else:
                choice = input(choice_text)
                if str(choice.lower()) == 'y'.lower():
                    generate_promocodes(prefix='TWERK', apply_promo=True)
                elif choice == '':
                    generate_promocodes(prefix='TWERK')
                else:
                    print("Такой опции нет")
            line_before()

        elif choice == '*':
            asyncio.run(genetare_for_all_games())
            line_before()

        elif choice == '9':
            print('Вы вышли в главное меню')
            return

        elif choice == '0':
            print("Выход")
            line_before()
            exit(1)

        else:
            print("Такой опции нет")
            line_before()
            print()


async def genetare_for_all_games():
    with open('Src/playground_games_data.json', 'r', encoding='utf-8') as f:
        apps = json.loads(f.read())['apps']

    choice = input(f"\nХотите применить промокоды после получения?\nY(да) / Enter(Нет): ")
    apply_promo = str(choice.lower()) == 'y'.lower()

    count = input(f"\nКоличество промокодов для всех игр Enter(по умолчанию 1): ")
    if count == '':
        count = 1
        print("\nКоличество промокодов не предоставлено. Генерируется 1 по умолчанию")

    if int(count) <= 0:
        logging.error(f"\nКоличество должно быть числом больше 0")
        exit(1)

    tasks = [hamster_client.get_promocodes(int(count), settings['send_to_group'], apply_promo, app["prefix"], settings['save_to_file']) for app in apps]
    await asyncio.gather(*tasks)
