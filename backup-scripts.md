# Back Up and Recover an Atlas Free Tier

## Backup de todas las bds
```sh
mongodump --uri <URI_DE_CONEXION> -o ./backup

mongorestore --uri <URI_DE_CONEXION> ./backup
```


## Backup de un bd especifica
```sh
mongodump --uri <URI_DE_CONEXION> -d <nombre_de_la_base_de_datos> -o ./backup

mongorestore --uri <URI_DE_CONEXION> ./backup --nsInclude='bd.*' 
```

## Exportar datos
```sh
mongoexport --uri <URI_DE_CONEXION> \
           -d football -c scorers \
           --query '{}' \
           --limit 5 \
           --out resultados.json
           --jsonFormat canonical
```
