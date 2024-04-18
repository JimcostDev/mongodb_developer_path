require('dotenv').config({ path: './config.env' });
const { MongoClient } = require('mongodb');
const readline = require('readline');

const MONGODB_URI = process.env.MONGODB_URI;
const client = new MongoClient(MONGODB_URI);
const dbname = 'football';
const collectionName = 'teams';

const connectToDatabase = async () => {
  try {
    await client.connect();
    console.log(`Connected to the ${dbname} database`);
  } catch (error) {
    console.error('Error connecting to the database', error);
  }
}

const main = async () => {
    try {
        await connectToDatabase();
        const db = client.db(dbname);
        const collection = db.collection(collectionName);

        const rl = readline.createInterface({
          input: process.stdin,
          output: process.stdout
        });

        let choice;
        do {
            console.log("\n\n1. Insertar un nuevo equipo");
            console.log("2. Mostrar todos los equipos");
            console.log("3. Buscar un equipo");
            console.log("4. Actualizar equipos");
            console.log("5. Eliminar un equipo");
            console.log("6. Salir");
            choice = await question(rl, "Elige una opción: ");

            switch (choice) {
                case '1':
                    await insertTeam(collection, rl);
                    break;
                case '2':
                    await showAllTeams(collection);
                    break;
                case '3':
                    await searchTeam(collection, rl);
                    break;
                case '4':
                    await updateTeams(collection, rl);
                    break;
                case '5':
                    await deleteTeam(collection, rl);
                    break;
                case '6':
                    console.log("Saliendo...");
                    break;
                default:
                    console.log("Opción no válida. Inténtalo de nuevo.");
            }
        } while (choice !== '6');

    } catch (error) {
        console.error('Error in the main function', error);
    } finally { 
        await client.close();
    }
}

const question = (rl, text) => {
  return new Promise((resolve, reject) => {
    rl.question(text, (answer) => {
      resolve(answer);
    });
  });
};

const insertTeam = async (collection, rl) => {
    const newTeam = {
        name: await question(rl, "Nombre del equipo: "),
        league: await question(rl, "Liga: "),
        country: await question(rl, "País: ")
    };
    const result = await collection.insertOne(newTeam);
    console.log("Equipo insertado con éxito:", result);
    return result;
}

const showAllTeams = async (collection) => {
    const teams = await collection.find({}).toArray();
    console.log("Equipos:");
    console.log(teams);
}

const searchTeam = async (collection, rl) => {
    const teamName = await question(rl, "Nombre del equipo a buscar: ");
    const query = { name: teamName };
    const team = await collection.findOne(query);
    console.log("Equipo encontrado:");
    console.log(team);
    return team;
}

const updateTeams = async (collection, rl) => {
    const league = await question(rl, "Liga a actualizar: ");
    const newLeague = await question(rl, "Nuevo nombre de la liga: ");
    const filter = { league: league };
    const update = { $set: { league: newLeague } };
    const updateResult = await collection.updateMany(filter, update);
    console.log("Equipos actualizados:", updateResult);
    return updateResult;
}

const deleteTeam = async (collection, rl) => {
    const teamName = await question(rl, "Nombre del equipo a eliminar: ");
    const query = { name: teamName };
    const deleteResult = await collection.deleteOne(query);
    console.log("Equipo eliminado:", deleteResult);
    return deleteResult;
}

main();
