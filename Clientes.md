from cliente import Cliente

def debe_fallar(**cambios):
    datos = dict(id_cliente="C001", nombre="Ana Pérez", documento="1012345678",
                 correo="ana@mail.com", telefono="3101234567")
    datos.update(cambios)
    try:
        Cliente(**datos)
    except ValueError as e:
        print(f"OK (error esperado): {e}")
    else:
        raise AssertionError(f"Debió fallar con {cambios}")


c = Cliente("C001", "  ana   pérez ", "1012345678", "ANA@Mail.com", "310 123 4567")
print(c)
assert c.nombre == "Ana Pérez" and c.correo == "ana@mail.com" and c.telefono == "3101234567"

debe_fallar(nombre="A1")
debe_fallar(documento="12ab")
debe_fallar(documento="123")
debe_fallar(correo="sin-arroba")
debe_fallar(telefono="2101234567")
debe_fallar(id_cliente="")

try:
    c.id_entidad = "X"
except AttributeError:
    print("OK: el id no se puede modificar (encapsulación)")

print("Todas las pruebas pasaron.") 
