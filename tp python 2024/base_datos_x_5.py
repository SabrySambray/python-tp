
def traer_productos(): #Esta base de datos sirve para el programa del cliente final y el del usuario administrador
    productos_db = [
    {
        "codigo": "1000",
        "nombre": "HAMBURGUESA CHEDDAR",
        "componentes": "Carne vacuna, queso cheddar en pan artesanal.",
        "categoria": "sánguches",
        "precio": "5120.00"
    },
    {
        "codigo": "1001",
        "nombre": "HAMBURGUESA C24",
        "componentes": "Carne vacuna, queso cheddar, salsa C24 en pan artesanal.",
        "categoria": "sánguches",
        "precio": "5427.00"
	},
    {
        "codigo": "1002",
        "nombre": "POLLO MONTY C24",
        "componentes": "Pechuga de pollo, salsa C24 en pan artesanal.",
        "categoria": "sánguches",
        "precio": "4468.00"
	},
    {
        "codigo": "1003",
        "nombre": "CHICKEN SANDWICH",
        "componentes": "Pechuga de pollo, mayonesa en pan artesanal.",
        "categoria": "sánguches",
        "precio": "3427.62"
	},
    {
        "codigo": "1004",
        "nombre": "QUE BUENA MOZZA",
        "componentes": "Hamburguesa con lechuga, tomate y mozzzarella en pan artesanal.",
        "categoria": "sánguches",
        "precio": "6475.65"
	},
    {
        "codigo": "1005",
        "nombre": "HAMBURCHICHA",
        "componentes": "Hamburguesa con queso cheddar y salchichas en pan artesanal.",
        "categoria": "sánguches",
        "precio": "6425.64"
    },
    {
        "codigo": "1006",
        "nombre": "CHORIBURGER CHEDDI",
        "componentes": "Chorizo mariposa doble con queso cheddar en pan artesanal.",
        "categoria": "sánguches",
        "precio": "4862.00"
    },
    {
        "codigo": "1007",
        "nombre": "CHIPANCHO",
        "componentes": "Pancho con salsa C24 en pan de chipá.",
        "categoria": "sánguches",
        "precio": "2769.23"
    },
	{
        "codigo": "1008",
        "nombre": "CHEDDAR FISH",
        "componentes": "Hamburguesa de brótola con queso cheddar en pan artesanal.",
        "categoria": "sánguches",
        "precio": "7411.00"
    },
	{
        "codigo": "1009",
        "nombre": "VEGGIE GARBANZOS",
        "componentes": "Hamburguesa de garbanzos con lechuga y tomate en pan artesanal.",
        "categoria": "sánguches",
        "precio": "5355.00"
        
    },
	{
        "codigo": "2000",
        "nombre": "FRITITAS",
        "componentes": "Papas fritas chicas.",
        "categoria": "guarniciones",
        "precio": "2714.00"
    },
	{
        "codigo": "2001",
        "nombre": "FRITEÑAS",
        "componentes": "Papas fritas medianas.",
        "categoria": "guarniciones",
        "precio": "3260.22"
    },
	{
        "codigo": "2002",
        "nombre": "FRITOTAS",
        "componentes": "Papas fritas grandes.",
        "categoria": "guarniciones",
        "precio": "4025.00"
    },
	{
        "codigo": "2003",
        "nombre": "FRANCISCANAS CHICAS",
        "componentes": "Papas rústicas fritas.",
        "categoria": "guarniciones",
        "precio": "2600.00"
    },
    {
        "codigo": "2004",
        "nombre": "FRANCISCANAS EN SU SALSA",
        "componentes": "Papas rústicas fritas con salsa cheddar.",
        "categoria": "guarniciones",
        "precio": "2850.00"
    },
	{
        "codigo": "2005",
        "nombre": "NUGGETS TWENTY",
        "componentes": "Nuggets de pollo - 20 unidades.",
        "categoria": "guarniciones",
        "precio": "3721.00"
    },
	{
        "codigo": "2006",
        "nombre": "OH ONION",
        "componentes": "Aros de cebolla.",
        "categoria": "guarniciones",
        "precio": "3286.00"
    },
	{
        "codigo": "2007",
        "nombre": "NOT FRENCH BRO",
        "componentes": "Papas fritas de brócoli.",
        "categoria": "guarniciones",
        "precio": "4674.21"
    },
	{
        "codigo": "2008",
        "nombre": "NOT FRENCH CARROT",
        "componentes": "Papas fritas de zanahoria.",
        "categoria": "guarniciones",
        "precio": "3565.00"
        
    },
	{
        "codigo": "3000",
        "nombre": "AGUA CON O SIN GAS",
        "componentes": "Agua con gas,agua sin gas.",
        "categoria": "bebidas",
        "precio": "1032.20"
    }, 
	{
        "codigo": "3001",
        "nombre": "PETIT SODA",
        "componentes": "Gaseosa de 275 ml.",
        "categoria": "bebidas",
        "precio": "2426.00"
    },
	{
        "codigo": "3002",
        "nombre": "MEDIUM SODA",
        "componentes": "Gaseosa de 500 ml.",
        "categoria": "bebidas",
        "precio": "3140.00"
	},   
    {
        "codigo": "3003",
        "nombre": "AGUA SABORIZADA",
        "componentes": "Botella de agua saborizada sin gas de 500 ml.", 
        "categoria": "bebidas",
        "precio": "1400.00"
    },     
    {
        "codigo": "3004",
        "nombre": "CERVEZA AMSTEL",
        "componentes": "Lata de cerveza de 473 ml.", 
        "categoria": "bebidas",
        "precio": "2600.00"
    },
	{	
        "codigo": "3005",
        "nombre": "PURA BUBBLE",
        "componentes": "Agua con gas de 275 ml.",
        "categoria": "bebidas",
        "precio": "2552.00"
	},
	{	
        "codigo": "3006",
        "nombre": "SANO JUICIO",
        "componentes": "Jugo natural de 275 ml.",
        "categoria": "bebidas",
        "precio": "3621.00"
	},
	{
        "codigo": "3007",
        "nombre": "STRONG MAN",
        "componentes": "Cerveza Warka de 575 ml.",
        "categoria": "bebidas",
        "precio": "7413.00"
	},
	{
        "codigo": "3008",
        "nombre": "RED BEARD BEER",
        "componentes": "Cerveza artesanal Barba Roja de 500 ml.",
        "categoria": "bebidas",
        "precio": "6154.00"
        
	},
	{
        "codigo": "4000",
        "nombre": "AVE CESAR",
        "componentes": "Ensalada de rúcula, parmesano en hebras.",
        "categoria": "ensaladas",
        "precio": "3280.00"
	},
	{
        "codigo": "4001",
        "nombre": "GUACA GUACA",
        "componentes": "Ensalada de rúcula, tomate, cebolla morada, guacamole.",
        "categoria": "ensaladas",
        "precio": "5176.00"
	},
	{
        "codigo": "4002",
        "nombre": "AL DENTE",
        "componentes": "Arroz yamaní, parmesano, tomate criollo, cruttons integrales.",
        "categoria": "ensaladas",
        "precio": "6274.00"
        
	},
	{
        "codigo": "4003",
        "nombre": "OLIVOS",
        "componentes": "Tomates pomarola, espinaca, queso fresco, aceitunas negras.",
        "categoria": "ensaladas",
        "precio": "7516.00"
	},
	{
        "codigo": "4004",
        "nombre": "BRIS",
        "componentes": "Tomates criollos, pepino, morrón amarillo, cebolla roja.",
        "categoria": "ensaladas",
        "precio": "4258.00"
	},
	{
        "codigo": "4005",
        "nombre": "NAMASU",
        "componentes": "Zanahoria, nabo daikon, alga kombu rehidratada.",
        "categoria": "ensaladas",
        "precio": "7325.00"
	},
	{
        "codigo": "4006",
        "nombre": "WALDORF",
        "componentes": "Apio, manzanas verdes, nueces, pasas de uva.",
        "categoria": "ensaladas",
        "precio": "6307.00"
	},
	{
        "codigo": "4006",
        "nombre": "VEGGIE C24",
        "componentes": "Lechuga, tomate, mozzarella, salsa C24, verduras asadas.",
        "categoria": "ensaladas",
        "precio": "5984.00"
        
    },
	{
        "codigo": "5000",
        "nombre": "MADNESS",
        "componentes": "Dos bochas helado con una salsa, crema y confites.", 
        "categoria": "postres",
        "precio": "4000.00"
	},
	{
        "codigo": "5001",
        "nombre": "OBVIO",
        "componentes": "Flan con dulce de leche.",
        "categoria": "postres",
        "precio": "3352.00"
	},
	{
		"codigo": "5002",
        "nombre": "VIGILANTE",
        "componentes": "Cuartirolo y membrillo.",
		"categoria": "postres",
        "precio": "4006.00"
	},
	{
		"codigo": "5003",
        "nombre": "MARRONCITOS",
        "componentes": "Brownies - 4 unidades.",
		"categoria": "postres",
        "precio": "3681.00"
	},
	{
		"codigo": "5004",
        "nombre": "ICE 2 ICE",
        "componentes": "Helado - 2 bochas.",
		"categoria": "postres",
        "precio": "2224.00"
	},
	{
		"codigo": "5005",
        "nombre": "PEACHAL",
        "componentes": "Duraznos en almibar.",
        "categoria": "postres",
        "precio": "1582.00"
	},
	{
        "codigo": "5006",
        "nombre": "SALTA LA LINDA",
        "componentes": "Dulce de chayote con quesadilla.",
		"categoria": "postres",
        "precio": "4769.00"
        
    }       
    ]
    return productos_db

 