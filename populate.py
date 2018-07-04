from random import randint
import subprocess
from time import sleep



############################
# MAIN
# Usage N = # of days in past you want to populate up to
# EX: populate.py 40 will populate last 40 days randomly with commits
############################

def main(argv):
	n = int(argv[0])
	i = 0
	while i <= n:
		num_commits = randint(0, 1)
		for commit in range(0, num_commits):
            subprocess.run(["touch", "realwork.txt"])
            with open("realwork.txt", "a") as f:
                f.write("new line\n")
            subprocess.run(["git", "add", "realwork.txt"])
            subprocess.run(["git", "commit", "--date=\"%s".format(str(i)), "day", "ago\"", "-m" "\"added real work\""])
            subprocess.run(["git", "push"])
			sleep(.5)
            subprocess.run("rm", "realwork.txt")
            subprocess.run(["git", "commit", "--date=\"%s".format(str(i)), "day", "ago\"", "-m" "\"removed real work\""])
            subprocess.run(["git", "push"])
			print("comittted")
		i += randint(0,4)

if __name__ == "__main__":
	main(sys.argv[1:])
