import subprocess
player1 = 23
player2 = 32
settings =  "{\"num_game\":1,\"max_round\":5,\"initial_stack\":10000,\"smallblind_amount\":20}"

outfile = open("subprocessOutput.txt","w")
errorfile = open("subprocessErrorOutput.txt","w")
timeout = 300
returncode = subprocess.call(["./tournamentScript.sh", str(player1),str(player2),settings,str(timeout)],
	stdout=outfile,stderr=errorfile)
outfile.close()
errorfile.close()
print(returncode)
if returncode:
	print("Error")
	outfile = open("subprocessErrorOutput.txt","r")
	result = outfile.read()
	return {"outcome":"Error","message":result}
else:
	print("Success")
	outfile = open("subprocessOutput.txt","r")
	result = outfile.read()
	if result == "Timeout\n":
		return {"outcome":"Timeout"}
	else:
		winner = result.split("'")[1]
		loser  =  result.split("'")[2]
		gap  =  int(result.split("'")[3])
		return {"outcome":"Win","winner":winner,"loser":loser,"profit":gap/2}