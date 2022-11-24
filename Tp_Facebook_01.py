# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------
#install this
#pip install termcolor
#pip install pyfiglet

import termcolor
import pyfiglet

def main():

	#Create Numbers
	numbers = input("Enter Your Numbers :")
	list_num = []
	#تكرار حتى يبقى رقم واحد
	while len(numbers)!=1:
		# لجمع الارقام
		sum_num = 0
		#فصل الارقام لجمعها
		for num in numbers:
			list_num.append(int(num))
		# sum جمعها بواسطه داله   
		sum_num = sum(list_num)

		#لعرض طريقه الجمع
		sum_affiche = '+'.join(numbers)
		#تصفيه المصفوفه
		list_num.clear()

		print(f"\nSum Your Numbers < {numbers} > ")
		print(f"{sum_num}={sum_affiche} ")
		numbers = str(sum_num)
	print(f"Last Nomber {sum_num}")
print(termcolor.colored(pyfiglet.figlet_format("@ddos_attack_co"), color="red"))

print(" Go to my Instagram account < @ddos_attack_co > and Fallowed Me \n Enter...", end="")
enter = input("")
main()

print(termcolor.colored(pyfiglet.figlet_format("THANCKS"), color="red"))
