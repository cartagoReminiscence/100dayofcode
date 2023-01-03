from simple_term_menu import TerminalMenu
from datetime import datetime
import time

def normalize_to_seconds(minutes, seconds):
	return minutes*60 + seconds

#LEAPS
LEAP_MINUTES = 0
LEAP_SECONDS = 9
LEAP_TOTAL_TIME = normalize_to_seconds(LEAP_MINUTES, LEAP_SECONDS)
#BREAKS
LONG_BREAK_MINUTES = 0
LONG_BREAK_SECONDS = 6
LONG_BREAK_TOTAL_TIME = normalize_to_seconds(LONG_BREAK_MINUTES, LONG_BREAK_SECONDS)

SHORT_BREAK_MINUTES = 0
SHORT_BREAK_SECONDS = 2
SHORT_BREAK_TOTAL_TIME = normalize_to_seconds(SHORT_BREAK_MINUTES, SHORT_BREAK_SECONDS)

def show_timestamp_start_to_end(total_time):
	print(f"start:\t{datetime.now()}")
	time.sleep(total_time)
	print(f"end:\t{datetime.now()}")
	print()

def banner(banner_text, number = 0):
	if(number != 0):
		banner_text += " " + str(number)
	banner_text = f"======= {banner_text} ======="
	print(banner_text)

def main():
	start_opt = "Start"
	break_opt = "Break"
	exit_opt = "Exit"
	options = [start_opt, break_opt, exit_opt]
	terminal_menu = TerminalMenu(options)

	num_of_leaps = 0
	num_of_breaks = 0

	selected = ""
	while(selected != exit_opt):
		menu_entry_index = terminal_menu.show()
		selected = options[menu_entry_index]
		if(selected == start_opt):
			num_of_leaps += 1
			banner("Leap no.", num_of_leaps)
			show_timestamp_start_to_end(LEAP_TOTAL_TIME)

		elif(selected == break_opt):
			num_of_breaks += 1
			if(num_of_breaks % 4 == 0):
				banner("Long break")
				show_timestamp_start_to_end(LONG_BREAK_TOTAL_TIME)
			else:
				banner("Break no.", num_of_breaks)
				show_timestamp_start_to_end(SHORT_BREAK_TOTAL_TIME)

		else:
			print(f"OK... See u later!")

if __name__ == "__main__":
    main()
