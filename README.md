## Guía para Configurar la API

Para comenzar, debemos crear una carpeta donde esté la API y debemos crear una carpeta llamada *environment*.

En esa carpeta, ejecutaremos este comando:

```bash
py -3.9 -m venv api_hexagonal
```

## Luego, ejecutaremos el siguiente comando para activar el entorno virtual:

```bash
api_hexagonal\Scripts\activate
```

## Ahora vamos a ir a la carpeta donde se encuentra la API y ejecutaremos este comando:

```bash
pip install -r requirements.txt
``` 
## Configuración del archivo .env

PUBLIC_KEY_MERCADOPAGO={Tu public key de Mercado Libre}
ACCESS_TOKEN_MERCADOPAGO={Tu clave de acceso de Mercado Libre}
DATABASE_URL={Tu URL de la base de datos}

## Y ya solo queda iniciar la API con el siguiente comando:


```bash
uvicorn app.main:app --reload
``` 



