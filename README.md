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