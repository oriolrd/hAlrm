import os

pwd = os.getcwd()

if not os.path.exists(pwd + "/motion"):
	os.makedirs(pwd + "/motion")


for i in range(0, 20):
	if not os.path.exists(pwd + "/motion/" + str(i)):
		os.makedirs(pwd + "/motion/" + str(i))
