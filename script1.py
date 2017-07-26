# My first real python script.
# Written by yomi
#
############### Define Variables #########################
#
amount=4		#Number of vessels.
vessels='glasses'	#Type of vessels used.
liquid='water'		#What is contained in the vessels.
location='on the table' #Location of vessels.
#
############## Output Variable Description ###############
#
print('This script has four variables pre-defined in it.')
print()
#
print('The variables are as follows:')
#
print("name: amount", "data type:", type(amount), "value:", amount, sep="\t")
#
print("name: vessels", "data type:", type(vessels), "value:", vessels, sep='\t')
#
print("name: liquid", "data type:", type(liquid), "value:", liquid, sep='\t')
#
print("name: location", "data type:", type(location), "value:", location, sep='\t')
print()
############## Output Sentence Using Variables ############
#
print("There are", amount, vessels, "full of", liquid, location, end='.\n')
print()
#

