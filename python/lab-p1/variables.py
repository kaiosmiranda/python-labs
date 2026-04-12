
# Armazena as informações do usuário
user = "kaiosmiranda"
age = 30
salary = 3000
rich = True if salary > 5000 else False

# Salário total liquido com descontos
INSS = salary * 0.11
liquido = salary - INSS

## Dados do usuário tratados
print(f"Usuário: {user}")
print(f"Idade: {age}")
print(f"Salário bruto: {salary} - {INSS} = {liquido}")
print(f"Rico?: {rich}")

# Tipos de variáveis que foram usadas para armazenar as informações
print("\nTipos de variáveis usadas")
print(f"Tipo de user: {type(user)}")
print(f"Tipo de age: {type(age)}")
print(f"Tipo de salary: {type(salary)}")
print(f"Tipo de rich: {type(rich)}")
print(f"Tipo de INSS: {type(INSS)}")

