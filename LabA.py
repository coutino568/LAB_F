debug= False

regexp1= "+^(??.*+"

regex2 = "ab*ab*"

regex3 ="a*b*a?"

ejercicio1 = "ab*ab*"
ejercicio2= "0?(1?)?0∗"
ejercicio2 = "(a*|b*)c"
ejercicio4= "(b|b)*abb(a|b)* "
ejercicio5 = "(a|ε)b(a+)c?"
ejercicio6 = "(a|b)*a(a|b)(a|b)"

symbolsTable = {
	"OR":"|",
	"AND":"^",
	"SUM":"+",
	"KLEENE":"*",
	"CONCATENATE":".",
	"QUESTION":"?"



}


#convierte una lsita de caracteres en un string
def listToString(list):
	stringed = ""
	for char in list:
		stringed += char
	return stringed


#Retorna la precedencia de un caracter individual
def getPrecedence(character):
	if(character=="("):
		return 1
	elif (character=="|"):
		return 2
	elif (character=="."):
		return 3
	elif (character=="?"):
		return 4
	elif (character=="*"):
		return 4
	elif (character=="+"):
		return 4
	elif (character=="^"):
		return 5
	else:
		return 6



##Formatea la expresion regular 
def formatRegEx(expresion):
	previousPrecedence =0
	currentPrecedence=0
	expressionList = []
	res = []
	allOperators = ["?","+","*","^","|"]
	binaryOperators = ["^","|"]
	#convertir string a lista para hacer pop y push
	for char in expresion:
		expressionList.append(char)
		#print(expressionList)

	#Recorre la lista
	for i in range(0, len(expressionList)):
		c1 = expressionList[i]
		if(debug):
			print("C1 is : " + c1)

		#evitar out of range	
		if(i+1 < len(expressionList)):
			c2 = expressionList[i+1]
			if(debug):
				print("C2 is : " + c2)

			res.append(c1)

			if(c1 != "(" and c2 != ")" and c2 not in allOperators and c1 not in binaryOperators):
				res.append(".")
	res.append(expressionList[-1])

	if(debug):
		print (" RES IS : "+ str(res))
	return res



#convierte la expresion regular a postfix
def infixToPostFix(expresion):
	print("EXPRESION REGULAR ES : " +str(expresion))


	formattedRegEx= formatRegEx(expresion)
	print("EXPRESION REGULAR FORMATEADA ES : " +str(listToString(formattedRegEx)))
	stack = []
	postfix=[]
	peekedCharPrecedence = getPrecedence(formattedRegEx[0])
	currentCharPrecedence= getPrecedence(formattedRegEx[0])
	


	for i in range (0, len(formattedRegEx)):
		
		char = formattedRegEx[i]
		if (char == "("):
			stack.append(char)
			#print("PUSHED " +str(char) + " To THE STACK")
			break
		elif(char ==")"):
			#print("PARENTESIS DE CIERRE")
			while (stack[-1] != "("):
				postfix.append(stack.pop())
			stack.pop()
			break

		else:
			while(len(stack)>0):
				peekedChar = stack[-1]
				peekedCharPrecedence = getPrecedence(peekedChar)
				currentCharPrecedence= getPrecedence(char)

				if (peekedCharPrecedence >= currentCharPrecedence):
					postfix.append(stack.pop())
				else:
					break

			stack.append(char)
		if(debug):
			print("CHAR : " + char + "|" + " STACK : "+str(stack) + " |POSTFIX" + str(postfix))
			print("PEEKED CHAR PRECEDENCE : " + str(peekedCharPrecedence)+" | CURRENT CHAR PRECEDENCE :" + str(currentCharPrecedence))
			print("")


	while (len(stack)>0):
		postfix.append(stack.pop())
	print("FINAL POSTFIX : " + str(listToString(postfix)))




def createTree(expresion):
	postfixExpression = infixToPostFix(expresion)
	# for i in range(0, len(postfixExpression)) :
	# 	if (i+1<= len(postfixExpression)):
	# 		c1 = postfixExpression[i]
	# 		c2 = postfixExpression[i+1]





#infixToPostFix(ejercicio1)





#infixToPostFix(regex2)

config = input("Desea ver el procedimiento? Y/N\n")
if(config=="Y"):
	debug = True


flag = True
while flag==True :
	expresion = input("Ingrese una expresion regular para formatear \nIngrese exit para salir\n")
	if expresion=="exit":
		flag = False
	else:
		createTree(expresion)


