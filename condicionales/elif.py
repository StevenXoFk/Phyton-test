plata = 80000
gasto = 90000

# If anidado y else if (elif)

if plata > 30000:
  if plata - gasto >= 20000:
    print("Bien económicamente ")
  elif plata - gasto < 0:
    print("Numeros rojos")
  elif plata - gasto < 20000:
    print("mal económicamente")
    
    
print(plata - gasto)