# Back Up and Recover an Atlas Free Tier

## Backup de todas las bds
mongodump --uri <URI_DE_CONEXION> -o ./backup
mongorestore --uri <URI_DE_CONEXION> ./backup

## Backup de un bd especifica
mongodump --uri <URI_DE_CONEXION> -d <nombre_de_la_base_de_datos> -o ./backup
mongorestore --uri <URI_DE_CONEXION> ./backup --db <nombre_de_la_base_datos>