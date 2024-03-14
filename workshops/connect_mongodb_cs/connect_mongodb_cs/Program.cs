using MongoDB.Driver;

var mongodbUri = "mongodb://localhost:27017/";

var client = new MongoClient(mongodbUri);

var dbList = client.ListDatabaseNames().ToList();

Console.WriteLine("La lista de bases de datos en el servidor es:");
foreach (var db in dbList)
{
    Console.WriteLine(db);
}