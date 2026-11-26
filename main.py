import dataset
inventario = dataset.connect("sqlite:///base.db")
productos = inventario["Productos"]

while True:
    opciones = input("\nA - Agregar\nL - Listar\nAC - Actualizar\nE - Eliminar producto\nS - Salir\n").upper()

    match opciones:

        case "A":   #Agregar productos
            agregarProducto = input("\nProducto: ").strip()
            agregarDescripcion = input("\nDescripcion: ").strip()
            agregarCantidad = int(input("\nCantidad del producto: ").strip())
            agregarPrecio = float(input("\nPrecio: ").strip())
            agregarCategoria = input("\nCategoria: ").strip()

            agregar = {"Nombre":agregarProducto,"Descripcion": agregarDescripcion,"Cantidad": agregarCantidad, "Precio": agregarPrecio,"Categoria":agregarCategoria}

            productos.insert(agregar)

        case "S":   #Salir
            break
        
        case "L":   #Listar productos
            for items in productos:
                print(f'ID:{items["id"]} | Producto: {items["Nombre"]} | Descripcion: {items["Descripcion"]} | Cantidad: {items["Cantidad"]} | Precio: {items["Precio"]} | Categoria: {items["Categoria"]}')
         
        case "E":  #Borrar por ID
            borrarID = int(input("\nID de prod. a borrar: ").strip())
            productos.delete(id=borrarID)
            
            print(f"\nEl producto cuyo ID es {borrarID} fue quitado con exito!!!\n")
               
        case "AC":  #Actualizar por ID
            idBuscar = int(input("\nIngrese ID a actualizar: "))
            
            nombreActualizar = input("\nNombre nuevo: ")
            descripcionActualizar = input("\nDescripcion nueva: ").strip()
            cantidadActualizar = int(input("\nCantidad del producto nueva: ").strip())
            precioActualizar = float(input("\nPrecio nuevo: "))
            catActualizar = input("\nCategoria nueva: ")
            
            actualizar = {"id":idBuscar,"Nombre":nombreActualizar, "descripcion":descripcionActualizar,"cantidad":cantidadActualizar,"Precio":precioActualizar,"Categoria":catActualizar}
            productos.upsert(actualizar,["id"])
