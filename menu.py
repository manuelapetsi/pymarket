"""Contains functions to display a menu for the main app"""
from db_func.menu_func import display_holdings, get_net_worth
# from db_func.backend_func import get_net_worth
import sys

def show_menu(user_id):
	print ('#'*80)
	print ('Please select which action you would like to take')
	print ('0) Quit')
	print ('1) Check holdings')
	print ('2) Update holdings')
	print ('3) Remove holdings')
	print ('4) Create new holding')
	selection = int(input())

	if selection not in range (0,5):	#if not valid selection, reselct
		print ('\n\n\nincorrect input please enter again')
		show_menu(user_id)

	if selection == 0:
		sys.exit()

	if selection == 1:	#check holdings
		check_holdings(user_id)

	if selection == 2:	#update holdings
		#display holdings 					function for this
		#choose which one to update using holdID
		pass

	if selection == 3:	#remove holdings
		#display holdings 					function for this
		#choose which to delete using holdID
		pass

	if selection == 4:	#create new holding
		pass



def check_holdings(user_id):	#selc 1
	print ("Here is a list of your holdings:\n")
	display_holdings(str(user_id))
	get_net_worth(str(user_id))
	print('\n\n\n\n')
	show_menu(user_id)

def update_holdings():
	#go to query file in db_Stuff
	#FUNCTION TO UPDATE HERE
	# sqlite> update holdings
 #   ...> set bought_at=1.27
 #   ...> where userID=1;
	pass

def remove_holdings():
	#go to query file in db_Stuff
	#FUNCTION TO DELETE HERE
	pass

def create_holding():
	#go to query file in db_Stuff
	#FUNCTION TO CREATE HOLDING
	pass