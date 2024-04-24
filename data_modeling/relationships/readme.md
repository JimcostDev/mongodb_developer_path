## Relaciones en BD:

Una relación en una base de datos se refiere **a la asociación entre dos conjuntos de datos**, donde los elementos de uno están conectados de alguna manera con los elementos del otro. Esta conexión puede representar dependencias lógicas, como la pertenencia de un objeto a otro, la ocurrencia de eventos relacionados, o cualquier otro tipo de vínculo significativo entre los datos. Las relaciones en una base de datos pueden tomar diversas formas, incluyendo uno a uno, uno a muchos y muchos a muchos, y son fundamentales para organizar y estructurar los datos de manera coherente y significativa.

En pocas palabras, son como **vínculos entre diferentes entidades** que contienen datos relacionados.

---
### Bases de datos relacionales o sql
--- 
### Relación uno a uno (1:1):
En una relación uno a uno (1:1), generalmente se establece la clave primaria de una tabla como clave foránea en la otra tabla. Por ejemplo, si tienes una tabla de "Persona" con una clave primaria llamada "ID_Persona", y otra tabla de "Pasaporte" con una clave primaria "ID_Pasaporte", podrías poner "ID_Persona" como clave foránea en la tabla de "Pasaporte", indicando que cada pasaporte está vinculado a una única persona. 
**La clave foránea puede ir en cualquiera de las dos tablas, en este caso no hay restricción específica.** Sin embargo, es común colocar la clave foránea en la tabla que representa la entidad secundaria de la relación, es decir, la tabla que tiene una sola ocurrencia en comparación con la otra. En el ejemplo dado, como cada pasaporte está vinculado a una única persona, colocaríamos la clave foránea "ID_Persona" en la tabla de "Pasaporte". Esto permite una navegación más intuitiva y eficiente de la relación.

#### Tabla: Persona

| ID_Persona | Nombre    | Apellido  | Edad | Ciudad   |
|------------|-----------|-----------|------|----------|
| 1          | Juan      | Pérez     | 30   | Ciudad A |
| 2          | María     | García    | 25   | Ciudad B |
| 3          | Carlos    | Martínez  | 35   | Ciudad C |
| ...        | ...       | ...       | ...  | ...      |

#### Tabla: Pasaporte

| ID_Pasaporte | Numero_Pasaporte | Fecha_Expedicion | ID_Persona |
|--------------|------------------|------------------|------------|
| 101          | PS123456789      | 2023-01-15       | 1          |
| 102          | PS987654321      | 2023-02-20       | 2          |
| 103          | PS456789123      | 2023-03-10       | 3          |
| ...          | ...              | ...              | ...        |

### Relación uno a muchos (1:N):
La clave primaria de la tabla "uno" se coloca como clave foránea en la tabla "muchos". Por ejemplo, si tienes una tabla de "Cliente" con "ID_Cliente" como clave primaria, y una tabla de "Órdenes" donde cada orden está asociada a un cliente, pondrías "ID_Cliente" como clave foránea en la tabla de "Órdenes". 

#### Tabla: Cliente

| ID_Cliente | Nombre     | Apellido   | Email             |
|------------|------------|------------|-------------------|
| 1          | Juan       | Pérez      | juan@example.com  |
| 2          | María      | García     | maria@example.com |
| 3          | Carlos     | Martínez   | carlos@example.com|
| ...        | ...        | ...        | ...               |

#### Tabla: Órdenes

| ID_Orden | Fecha       | Total    | ID_Cliente |
|----------|-------------|----------|------------|
| 101      | 2023-01-15  | 150.00   | 1          |
| 102      | 2023-02-20  | 200.00   | 2          |
| 103      | 2023-03-10  | 100.00   | 1          |
| ...      | ...         | ...      | ...        |

### Relación muchos a muchos (N:N):
En una relación muchos a muchos (N:N), generalmente se necesita una tabla intermedia para establecer la relación. Esta tabla intermedia contiene las claves primarias de las tablas que están siendo relacionadas. Por ejemplo, si tienes una relación entre las tablas "Estudiante" y "Clase", donde un estudiante puede estar inscrito en muchas clases y una clase puede tener muchos estudiantes, necesitarías una tabla intermedia como "Inscripción" que contenga las claves primarias de "Estudiante" y "Clase", además de cualquier otro dato relevante, como la fecha de inscripción.

## Tabla: Estudiante

| ID_Estudiante | Nombre     | Apellido  | Edad | Email             |
|---------------|------------|-----------|------|-------------------|
| 1             | Juan       | Pérez     | 20   | juan@example.com  |
| 2             | María      | García    | 22   | maria@example.com |
| 3             | Carlos     | Martínez  | 21   | carlos@example.com|
| ...           | ...        | ...       | ...  | ...               |

## Tabla: Clase

| ID_Clase | Nombre    | Profesor  | Horario    |
|----------|-----------|-----------|------------|
| 101      | Matemáticas| Dr. López | L-M-W 9am  |
| 102      | Historia  | Dra. Gómez| M-J 1pm    |
| 103      | Física    | Prof. Díaz| M-W-F 11am |
| ...      | ...       | ...       | ...        |

## Tabla: Inscripción

| ID_Inscripcion | ID_Estudiante | ID_Clase | Fecha_Inscripcion |
|----------------|---------------|----------|------------------|
| 1              | 1             | 101      | 2023-01-15       |
| 2              | 1             | 103      | 2023-02-20       |
| 3              | 2             | 101      | 2023-03-10       |
| ...            | ...           | ...      | ...              |

--- 
### Bases de datos NoSql (MongoDB):
--- 
En MongoDB, el enfoque para modelar relaciones es un poco diferente debido a su estructura de base de datos NoSQL orientada a documentos. 

### Relación uno a uno (1:1):
Para una relación uno a uno en MongoDB, podrías embeber un documento dentro de otro. Por ejemplo, si tienes una colección de "Personas" y cada persona tiene un único pasaporte, podrías embeber la información del pasaporte dentro del documento de la persona. 
Es asi para la mayoria de casos; si el documento es muy grande y puede que supere el tamaño permitido (16MB), en este caso es mejor referenciar.

```js
// Colección: Personas
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c5"),
  "nombre": "Juan",
  "apellido": "Pérez",
  "edad": 30,
  "ciudad": "Ciudad A",
  "pasaporte": {
    "numero": "PS123456789",
    "fecha_expedicion": ISODate("2023-01-15")
  }
}

```

### Relación uno a muchos (1:N):
Para una relación uno a muchos, puedes utilizar un array de documentos embebidos o hacer referencia al documento principal utilizando su ID. Por ejemplo, si tienes una colección de "Clientes" y cada cliente puede tener múltiples órdenes, podrías almacenar las órdenes como un array dentro del documento del cliente o almacenar solo los IDs de las órdenes relacionadas en el documento del cliente.
##### Usando un array de documentos embebidos:
```js
// Colección: Clientes
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c5"),
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan@example.com",
  "ordenes": [
    {
      "id_orden": ObjectId("6098b48e5baf7d001f2b71c6"),
      "fecha": ISODate("2023-01-15"),
      "total": 150.00
    },
    {
      "id_orden": ObjectId("6098b48e5baf7d001f2b71c7"),
      "fecha": ISODate("2023-02-20"),
      "total": 200.00
    }
  ]
}
```
##### Usando referencias a los IDs de las órdenes:
```js
// Colección: Clientes
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c5"),
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan@example.com",
  "ordenes": [
    ObjectId("6098b48e5baf7d001f2b71c6"),
    ObjectId("6098b48e5baf7d001f2b71c7")
  ]
}
```
> La elección entre **embeber documentos y utilizar referencias** depende de factores como la frecuencia y la forma en que accedes a los datos, el tamaño de los documentos y la necesidad de realizar consultas complejas.

### Relación muchos a muchos (N:N):
Para relaciones muchos a muchos, también puedes utilizar arrays de IDs o documentos embebidos en ambas colecciones para representar la relación. Por ejemplo, si tienes una colección de "Estudiantes" y otra de "Clases", podrías almacenar los IDs de las clases en las que está inscrito un estudiante en un array dentro del documento del estudiante, y viceversa.

##### Usando arrays de IDs:
```js
// Colección: Estudiantes
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c5"),
  "nombre": "Juan",
  "apellido": "Pérez",
  "clases_inscritas": [
    ObjectId("6098b48e5baf7d001f2b71c6"),
    ObjectId("6098b48e5baf7d001f2b71c7")
  ]
}

// Colección: Clases
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c6"),
  "nombre": "Matemáticas",
  "profesor": "Dr. López",
  "horario": "L-M-W 9am",
  "estudiantes_inscritos": [
    ObjectId("6098b48e5baf7d001f2b71c5"),
    ObjectId("6098b48e5baf7d001f2b71c8")
  ]
}
```

##### Usando documentos embebidos:
```js
// Colección: Estudiantes
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c5"),
  "nombre": "Juan",
  "apellido": "Pérez",
  "clases_inscritas": [
    {
      "id_clase": ObjectId("6098b48e5baf7d001f2b71c6"),
      "nombre": "Matemáticas",
      "profesor": "Dr. López",
      "horario": "L-M-W 9am"
    },
    {
      "id_clase": ObjectId("6098b48e5baf7d001f2b71c7"),
      "nombre": "Historia",
      "profesor": "Dra. Gómez",
      "horario": "M-J 1pm"
    }
  ]
}

// Colección: Clases
{
  "_id": ObjectId("6098b48e5baf7d001f2b71c6"),
  "nombre": "Matemáticas",
  "profesor": "Dr. López",
  "horario": "L-M-W 9am",
  "estudiantes_inscritos": [
    {
      "id_estudiante": ObjectId("6098b48e5baf7d001f2b71c5"),
      "nombre": "Juan",
      "apellido": "Pérez"
    },
    {
      "id_estudiante": ObjectId("6098b48e5baf7d001f2b71c8"),
      "nombre": "María",
      "apellido": "García"
    }
  ]
}
```
---
No existe una regla general estricta sobre cuándo embeber o referenciar en una base de datos. La decisión depende principalmente de la naturaleza de los datos y de los requisitos específicos de la aplicación. 

Nos podemos guiar con las siguientes preguntas:

1. ¿Qué tan frecuente es consultada la información?
2. ¿Qué tan frecuente se actualiza la información?
3. ¿La información se consulta en conjunto en partes?


**Embeber:** 
- Útil cuando los datos embebidos **son naturalmente parte del documento principal y siempre se acceden juntos.**
- Adecuado para **relaciones uno a uno o uno a pocos**, donde los datos embebidos son relativamente pequeños y no cambian frecuentemente.
- Puede mejorar el rendimiento de consultas al reducir la necesidad de unir múltiples colecciones.

**Referenciar:**
- Adecuado cuando los datos relacionados **pueden ser compartidos por múltiples documentos o pueden cambiar frecuentemente.**
- Útil para relaciones **uno a muchos o muchos a muchos**, donde los datos relacionados son grandes o pueden ser actualizados independientemente.
- Permite una gestión más eficiente de los datos relacionados y puede mantener la consistencia en toda la base de datos.

En general, es importante considerar la consistencia, la integridad y el rendimiento al tomar decisiones sobre cómo modelar las relaciones en la base de datos. A menudo, es una cuestión de equilibrar estos factores y adaptar el enfoque según las necesidades específicas del proyecto.
