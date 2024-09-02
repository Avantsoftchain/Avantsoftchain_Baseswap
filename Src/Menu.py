from Src.Colors import *
from Src.db_SQlite import ConfigDB
from Src.Login import hamster_client
from Src.utils import get_status, get_games_data, remain_time, localized_text

config = ConfigDB()
lang = config.lang


def main_menu():
    activities = hamster_client()._activity_cooldowns()
    taps_status = task_status = cipher_status = combo_status = 'n/a'
    taps_cooldown = task_cooldown = cipher_cooldown = combo_cooldown = 'n/a'

    if activities:
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

    if config.hamster_token:
        menu = (
            f"📚  Главное меню \n"
            f"  Какую активность хотите выполнить? \n"
            f"  {LIGHT_YELLOW}# |  {RESET}📝 {YELLOW}Информация {WHITE} \n"
            f"  {LIGHT_YELLOW}1 |  {RESET}👆 {YELLOW}Клики {WHITE}       {taps_status} · Осталось: {taps_cooldown} \n"
            f"  {LIGHT_YELLOW}2 |  {RESET}📑 {YELLOW}Задания {WHITE}     {task_status} · Осталось: {task_cooldown} \n"
            f"  {LIGHT_YELLOW}3 |  {RESET}🔍 {YELLOW}Шифр {WHITE}        {cipher_status} · Осталось: {cipher_cooldown} \n"
            f"  {LIGHT_YELLOW}4 |  {RESET}💰 {YELLOW}Комбо {WHITE}       {combo_status} · Осталось: {combo_cooldown} \n"
            f"  {LIGHT_YELLOW}5 |  {RESET}🔑 {YELLOW}Миниигры {WHITE} \n"
            f"  {LIGHT_YELLOW}6 |  {RESET}🎁 {YELLOW}Промокоды {WHITE} \n"
            f"  {LIGHT_YELLOW}a |  {RESET}🔐 {YELLOW}Аккаунты {WHITE} \n"
            f"  {LIGHT_YELLOW}$ |  {RESET}💲 {YELLOW}Список самых выгодных карт {WHITE} \n"
            f"  {LIGHT_YELLOW}+ |  {RESET}⭐️ {YELLOW}Купить карту `+ID_Карты` (напрмиер +dao) {WHITE} \n"
            f"  {LIGHT_YELLOW}s |  {RESET}🛠 {YELLOW}Настройки {WHITE} \n"
            f"  {LIGHT_YELLOW}m |  {RESET}📝 {YELLOW}Показать меню {WHITE} \n"
            f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW}Выйти{WHITE}"
        )

    else:
        menu = localized_text('main_menu_not_logged', lang, light_yellow=LIGHT_YELLOW, reset=RESET, yellow=YELLOW, white=WHITE)
        # menu = (
        #     f"Главное меню \n"
        #     f"  Какую активность хотите выполнить? \n"
        #     f"  {LIGHT_YELLOW}6 |  {RESET}🎁 {YELLOW}Промокоды {WHITE}    \n"
        #     f"  {LIGHT_YELLOW}m |  {RESET}📝 {YELLOW}Показать меню {WHITE} \n"
        #     f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW}Выйти{WHITE}"
        # )
    print(f"{menu.strip()} \n")


def playground_menu():
    promos = []
    if config.hamster_token:
        promos = hamster_client()._get_promos()

    keys_per_day = 4
    games_data = get_games_data()['apps']
    games_info = {game['title']: {"emoji": game['emoji'], "color": LIGHT_YELLOW} for game in games_data}
    max_width = max(len(game) for game in games_info)

    for promo in promos:
        game_name = promo['name']
        if game_name in games_info:
            games_info[game_name].update({
                "keys": promo['keys'],
                "cooldown": promo['remain'],
                "status": get_status(promo['isClaimed'])
            })

    menu = "🎮  Игровая площадка \n  Для какой игры хотите получить промокоды? \n"
    for i, (game_name, game_data) in enumerate(games_info.items(), start=1):
        keys = game_data.get("keys", 0)
        cooldown = game_data.get("cooldown", "n/a")
        status = game_data.get("status", f"{RED}❌{WHITE}")
        emoji = game_data["emoji"]
        color = game_data["color"]

        menu += (f"  {LIGHT_YELLOW}{i} |  {RESET}{emoji} {YELLOW} {color}{game_name:<{max_width}} {WHITE}  "
                 f"{keys}/{keys_per_day}  {status} · Осталось: {cooldown} \n")

    menu += (
        f"  {LIGHT_YELLOW}* |  {RESET}🎉 {YELLOW} Для всех игр {WHITE} \n"
        f"  {LIGHT_YELLOW}< |  {RESET}🔙 {YELLOW} В главное меню {WHITE} \n"
        f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW} Выйти {WHITE} \n"
    )
    print(menu.strip())


def minigames_menu():
    minigames = []
    if config.hamster_token:
        minigames = hamster_client()._get_minigames()

    games_data = get_games_data()['minigames']
    games_info = {game['title']: {"emoji": game['emoji'], "color": LIGHT_YELLOW} for game in games_data}
    max_width = max(len(game) for game in games_info)

    for minigame in minigames:
        game_name = minigame['id']
        if game_name in games_info:
            games_info[game_name].update({
                "cooldown": minigame['remainSeconds'],
                "status": get_status(minigame['isClaimed'])
            })

    menu = "🎮  Миниигры \n  Какую миниигру хотите пройти? \n"
    for i, (game_name, game_data) in enumerate(games_info.items(), start=1):
        cooldown = remain_time(game_data.get("cooldown", "n/a"))
        status = game_data.get("status", "n/a")
        emoji = game_data["emoji"]
        color = game_data["color"]

        menu += f"  {LIGHT_YELLOW}{i} |  {RESET}{emoji} {YELLOW} {color}{game_name:<{max_width}} {WHITE}  {status} · Осталось: {cooldown} \n"

    menu += (
        f"  {LIGHT_YELLOW}< |  {RESET}🔙 {YELLOW} В главное меню {WHITE} \n"
        f"  {LIGHT_YELLOW}0 |  {RESET}🔚 {YELLOW} Выйти {WHITE} \n"
    )
    print(menu.strip())


def settings_menu():
    send_to_group = get_status(config.send_to_group)
    apply_promo = get_status(config.apply_promo)
    save_to_file = get_status(config.save_to_file)
    spinner = config.spinner

    menu = (
        f"🛠  Настройки \n"
        f"  {LIGHT_YELLOW}1 | {RESET}{YELLOW} Отправлять в группу:  {send_to_group} (включить/отключить) {WHITE} \n"
        f"  {LIGHT_YELLOW}2 | {RESET}{YELLOW} Применять промокоды:  {apply_promo} (включить/отключить) {WHITE} \n"
        f"  {LIGHT_YELLOW}3 | {RESET}{YELLOW} Сохранять в файл:     {save_to_file} (включить/отключить) {WHITE} \n"
        f"  {LIGHT_YELLOW}  | {RESET}{YELLOW} Спиннер:              {spinner}{WHITE} (spinner_<name> · <name>/default/list) \n"
    )
    print(menu.strip())
