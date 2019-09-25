def Int_Check(String):
	try:
		int(String)
		return True
	except ValueError:
		return False
