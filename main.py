from authorizer import Authorizer

# Una vez el sistema reciba una notificacion del usuario se llama a la clase
# Authorizer para poder saber si el usuario queda autenticado o no
auth = Authorizer()
checkUserStatus = auth.verify('', 'user: admin password: ***', '181.139.254.197')

if (checkUserStatus):
    print('El usuario ha accedido exitosamente')
else:
    print('El usuario no ha podido acceder al sistema')