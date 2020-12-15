
def checkpassword(password):

  if((len(password) < 8) or (any(char.isdigit() for char in password)) == False or (any(char.isupper() for char in password)) == False or  (any(char.islower() for char in password)) == False):
    return "A senha não está boa"
  else: return "Good password"

if __name__ == "__main__":
  password = input("Coloque sua senha ")
  print("\n{}".format(checkpassword(password)))