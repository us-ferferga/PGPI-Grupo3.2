## Desarrollo del backend

[Información importante a la hora de crear controladores](https://github.com/us-ferferga/PGPI-Grupo3.2/blob/master/backend/TraineerbookApp/views.py#L21-L57)

## Ejecución del contenedor

Dado un archivo tar.gz, hay que cargar la imagen en el sistema (se asume sistema Linux):

```
docker load < imagen.tar.gz
```

Para ponerla en funcionamiento:

```
docker run [...parámetros] traineerbook
```

Si se usa la imagen subida al repositorio y no un ``tar.gz``,
reemplazar por ``ghcr.io/us-ferferga/traineerbook``

---

Para hacer que el servicio esté disponible en el host,
añadir el siguiente parámetro:

```
-p PUERTO_DESEADO:80
```

---

Para persistir la información cuando se detenga el contenedor,
se debe de montar la carpeta /data del contenedor. Añadir:

```
-v ./datos:/data
```
Esto creará una carpeta ``datos`` en el directorio actual en el que se encuentre la terminal.
**Es importante que en la primera ejecución este directorio esté vacío o los datos de prueba no
se cargarán correctamente**

---

Se puede personalizar el *username* y el *email* del superadministrador. **Solo tienen efecto la primera vez,
al crear los datos iniciales**.Estos son los valores por defecto:

```
-e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_EMAIL=r@root.com -e DJANGO_SUPERUSER_PASSWORD=root
```
