import shutil
import time

def get_day_counter(filename):
	day_counter_file_read = open(filename, 'r')
	day_file_counter = int(day_counter_file_read.read())
	day_counter_file_read.close()
	return day_file_counter

def increment_day_counter(filename, day_counter):
	day_counter += 1
	day_counter_file_add = open(filename, 'w')
	day_counter_file_add.write(str(day_counter))
	day_counter_file_add.close()

def reset_day_counter(filename):
	day_counter = 1
	day_counter_file_add = open(filename, 'w')
	day_counter_file_add.write(str(day_counter))
	day_counter_file_add.close()

def copy_log_file(auth_log_file, auth_log_dest):
	current_date = time.strftime("%m-%d-%Y")
	auth_log_file_final = auth_log_dest + "auth-" + str(current_date) + ".log"
	shutil.copyfile(auth_log_file, auth_log_file_final)

def main():
	auth_log_dir = "/var/log/auth.log"
	dest_log_dir = "/home/destinesavior/auth-logs/"
	day_counter = get_day_counter('day_counter.txt')

	if (day_counter == 3):
		copy_log_file(auth_log_dir, dest_log_dir)
		reset_day_counter('day_counter.txt')
	else:
		increment_day_counter('day_counter.txt', day_counter)


if __name__ == '__main__':
	main()


