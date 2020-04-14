import sys

def esDivisor(n, m):
  '''
  Retorna si `m` es divisor de `n`.
  '''
  return n % m == 0

def esPrimo(n):
  '''
  Determina si `n` es un numero primo o no.
  Tanto el 0 como el 1 son tratados de forma especial, y no son primos.

  `n` es un numero natural
  '''
  if n == 0 or n == 1:
    return False

  # Cuenta la cantidad de divisores enteros que tiene `n`, luego
  # analiza la condicion de primo para retornar su caracter.
  i = 1
  divisor_count = 0
  while i <= n:
    if esDivisor(n, i):
      divisor_count = divisor_count + 1
    i += 1
  return True if divisor_count == 2 else False

def iesimoPrimo(i):
  '''
  Retorna el i-esimo numero primo. El primero es 2.

  `i` es un numero natural.

  Consulta si n es primo desde 2 hasta encontrar el i-esimo
  numero primo.
  '''
  prime_count = 0
  n = 1
  while prime_count != i:
    n = n + 1
    if esPrimo(n):
      prime_count = prime_count + 1
  return n

def cantidadPrimosMenoresOIguales(n):
  '''
  Retorna la cantidad de numeros primos menores o iguales a `n`. 

  `n` es un numero natural.
  '''
  count_primes = 0
  number = 1
  while number <= n:
    if esPrimo(number):
      count_primes = count_primes + 1
    number = number + 1
  return count_primes

def cantidadDivisoresPrimos(n):
  '''
  Retorna la cantidad de divisores primos de `n`
  '''
  count_divisor = 0
  prime_index = 1
  prime_divisor = iesimoPrimo(prime_index)

  # Itera en numeros primos evaluando si son divisores de `n`
  # hasta que el divisor sea mayor que `n`.
  while prime_divisor <= n:
    if esDivisor(n, prime_divisor):
      count_divisor = count_divisor + 1
    prime_index = prime_index + 1 
    prime_divisor = iesimoPrimo(prime_index)

  return count_divisor

def iesimoDivisorPrimo(n, i):
  '''
  Retorna el `i`-esimo divisor primo de `n`.
  Retorna 0 cuando:
    - `i` es mayor a la cantidad de divisores primos de `n`, o
    - `i` es menor a 1, o
    - `n` es menor o igual a 1
  '''
  # Analizo prerrequisitos.
  num_prime_divisors = cantidadDivisoresPrimos(n)
  if i > num_prime_divisors or i < 1 or n <= 1:
    return 0

  # Condicion de entrada del ciclo
  count_divisor = 0
  prime_index = 1
  # Itero en los numeros primos que son divisores de `n`, 
  # hasta obtener el i-esimo
  while count_divisor < i:
    prime_divisor = iesimoPrimo(prime_index)
    prime_index = prime_index + 1
    if esDivisor(n, prime_divisor):
      count_divisor = count_divisor + 1
  
  return prime_divisor

def sumaPrimerosPrimos(n):
  '''
  Rertorna la suma de los primeros `n` numeros primos de forma recursiva.
  '''
  if n <= 0:
    return 0
  if n == 1:
    return iesimoPrimo(1)
  return iesimoPrimo(n) + sumaPrimerosPrimos(n - 1)


def test_esPrimo():
  assert False == esPrimo(0)
  assert False == esPrimo(1)
  assert True == esPrimo(2)
  assert True == esPrimo(3)
  assert False == esPrimo(4)
  assert True == esPrimo(5)
  assert False == esPrimo(6)
  assert True == esPrimo(7)
  assert False == esPrimo(8)
  assert False == esPrimo(9)
  assert False == esPrimo(10)
  assert True == esPrimo(23)

def test_iesimoPrimo():
  assert 2 == iesimoPrimo(1)
  assert 3 == iesimoPrimo(2)
  assert 11 == iesimoPrimo(5)
  assert 71 == iesimoPrimo(20)

def test_cantidadPrimosMenoresOIguales():
  assert 0 == cantidadPrimosMenoresOIguales(1)
  assert 1 == cantidadPrimosMenoresOIguales(2)
  assert 2 == cantidadPrimosMenoresOIguales(3)
  assert 3 == cantidadPrimosMenoresOIguales(6)
  assert 4 == cantidadPrimosMenoresOIguales(7)

def test_cantidadDivisoresPrimos():
  assert 0 == cantidadDivisoresPrimos(0)
  assert 0 == cantidadDivisoresPrimos(1)
  assert 1 == cantidadDivisoresPrimos(2)
  assert 1 == cantidadDivisoresPrimos(3)
  assert 1 == cantidadDivisoresPrimos(4)
  assert 1 == cantidadDivisoresPrimos(5)
  assert 2 == cantidadDivisoresPrimos(6)
  assert 1 == cantidadDivisoresPrimos(7)

def test_iesimoDivisorPrimo():
  assert 2 == iesimoDivisorPrimo(2, 1)
  assert 0 == iesimoDivisorPrimo(2, 2)
  assert 2 == iesimoDivisorPrimo(10, 1)
  assert 5 == iesimoDivisorPrimo(10, 2)
  assert 2 == iesimoDivisorPrimo(30, 1)
  assert 3 == iesimoDivisorPrimo(30, 2)
  assert 5 == iesimoDivisorPrimo(30, 3)

def test_sumaPrimerosPrimos():
  assert 0 == sumaPrimerosPrimos(0)
  assert 2 == sumaPrimerosPrimos(1)
  assert 5 == sumaPrimerosPrimos(2)
  assert 10 == sumaPrimerosPrimos(3)
  assert 28 == sumaPrimerosPrimos(5)

def test_all():
  test_esPrimo()
  test_iesimoPrimo()
  test_iesimoDivisorPrimo()
  test_cantidadDivisoresPrimos()
  test_cantidadPrimosMenoresOIguales()
  test_sumaPrimerosPrimos()

if sys.argv[1] == 'test':
  test_all()
  print('All tests passed successfully')
elif sys.argv[1] == 'esPrimo':
  if esPrimo(int(sys.argv[2])):
    print('si')
  else:
    print('no')
elif sys.argv[1] == 'iesimoPrimo':
  print(iesimoPrimo(int(sys.argv[2])))
elif sys.argv[1] == 'cantidadPrimosMenoresOIguales':
  print(cantidadPrimosMenoresOIguales(int(sys.argv[2])))
elif sys.argv[1] == 'cantidadDivisoresPrimos':
  print(cantidadDivisoresPrimos(int(sys.argv[2])))
elif sys.argv[1] == 'iesimoDivisorPrimo':
  divisor = iesimoDivisorPrimo(int(sys.argv[2]), int(sys.argv[3]))
  if divisor != 0:
    print(divisor)
  else:
    print(sys.argv[2] + ' no tiene ' + sys.argv[3] + ' divisores primos')
elif sys.argv[1] == 'sumaPrimerosPrimos':
  print(sumaPrimerosPrimos(int(sys.argv[2])))
