# Usuarios de mongo:

## Usuario *admin*:
    - Permisos: Todos
    - User: root
    - Password: root

### Creacion:
```JSON
db.createUser({
    user: "root",
    pwd:"root",
    roles:[{
            role:"userAdminAnyDatabase",
            db:"admin"
        }] 
});
```

## Usuario *connector*:
    - Permisos: Solo lectura
    - User: connector
    - Password: password

### Creacion:
```JSON
db.createUser({
    user: "connector",
    pwd:"password",
    roles:[{
            role:"read",
            db:"newBtc"
        }] 
});
```

## Equipo
- Armando Elías Aguirre Sosa 		1112150023
- Efraín Fernando Bejarano Puentes 	1119150056
- Rosa Alejandra Legarda Bencomo 	1119150016
- Emmanuel Campuzano Contreras 	1119150081
