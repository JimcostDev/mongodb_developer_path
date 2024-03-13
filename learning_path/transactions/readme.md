# Transacciones ACID en MongoDB:

## Transacción:

Una transacción es una unidad de trabajo que agrupa una serie de operaciones en una sola acción. En el contexto de una base de datos, una transacción se refiere a un conjunto de operaciones que se ejecutan juntas como una sola unidad, ya sea que todas se completen con éxito o ninguna.

## ACID:

ACID es un acrónimo que describe las cuatro propiedades clave que debe cumplir una transacción para garantizar la integridad de los datos:

Imagina que estás en una tienda y quieres comprar dos manzanas.

- **Atomicidad:** Quieres que ambas manzanas se agreguen a tu bolsa al mismo tiempo. Si solo se agrega una, no es una compra completa. En MongoDB, las transacciones ACID garantizan que todas las operaciones dentro de una transacción se completen o ninguna.

- **Consistencia:** Las manzanas deben estar disponibles en el inventario de la tienda para que puedas comprarlas. En MongoDB, las transacciones ACID garantizan que la base de datos se mantenga en un estado consistente después de cada transacción.

- **Aislamiento:** Tu compra no debe verse afectada por lo que otros clientes estén comprando. En MongoDB, las transacciones ACID protegen tus datos de accesos concurrentes, asegurando que tu operación se complete sin interferencias.

- **Durabilidad:** Una vez que pagas las manzanas, la compra se registra de forma permanente. En MongoDB, las transacciones ACID aseguran que los datos se almacenen de forma permanente incluso en caso de fallos del sistema.

## En resumen:

Las transacciones ACID en MongoDB te permiten realizar operaciones complejas en varios documentos con la seguridad de que se completarán de forma consistente, segura y permanente.
Es como si cada transacción fuera una caja individual que protege tus datos y los mantiene en un estado coherente.

## Ejemplo:

Supongamos que tienes una tienda online y quieres actualizar el stock de un producto después de una venta. Puedes usar una transacción ACID para:

- Reducir la cantidad de stock en 1.
- Registrar la venta en la base de datos.

Si la transacción falla, no se modifica el stock ni se registra la venta, lo que mantiene la integridad de tus datos.

## Beneficios:

- Mayor seguridad y confiabilidad de los datos.
- Mayor precisión en operaciones complejas.
- Mejor rendimiento y escalabilidad.

## Limitaciones:

- Las transacciones ACID pueden ser más lentas que las operaciones sin transacciones.
- No todas las operaciones de MongoDB son compatibles con las transacciones ACID.

En resumen, las transacciones ACID en MongoDB son una herramienta poderosa para garantizar la integridad y la seguridad de tus datos en operaciones complejas.
