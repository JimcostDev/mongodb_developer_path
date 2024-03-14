using MongoDB.Bson;
using MongoDB.Driver;

var mongodbUri = "mongodb://localhost:27017/";

var client = new MongoClient(mongodbUri);

var dbList = client.ListDatabaseNames().ToList();

Console.WriteLine("La lista de bases de datos en el servidor es:");
foreach (var db in dbList)
{
    Console.WriteLine(db);
}


// CRUD
var database = client.GetDatabase("api_menu_db");
var categoriesCollection = database.GetCollection<BsonDocument>("categories");

// insertar documento
var document = new BsonDocument
{
    {"name", "Hamburguesas" },
    {"image","url_de_la_imagen" }
};
categoriesCollection.InsertOne(document);


// actualizar un documento
var filter = Builders<BsonDocument>.Filter.Eq("name", "Hamburguesas");
var update = Builders<BsonDocument>.Update.Set("name", "PASTA");

var result = categoriesCollection.UpdateOne(filter, update);
Console.WriteLine(result.IsAcknowledged);

// eliminar un documento
var filterToDelete = Builders<BsonDocument>.Filter.Eq("name", "PASTA");
categoriesCollection.DeleteOne(filterToDelete);

// buscar documentos
var categories = categoriesCollection.Find(_ => true).ToList();
foreach (var category in categories)
{
    Console.WriteLine(category.ToString());
}