// Importa dependencias
const express = require('express');
const cors = require('cors');
const sequelize = require('./database'); // Importa la configuración de Sequelize

// Importa rutas
const itemRoutes = require('./routes/routes');

const app = express();
app.use(cors());
app.use(express.json());

// Sincroniza la base de datos
sequelize.sync()
    .then(() => {
        console.log('Conectado a la base de datos MySQL y modelos sincronizados');
    })
    .catch((err) => {
        console.error('Error al sincronizar la base de datos:', err);
    });

// Usa las rutas
app.use('/api/items', itemRoutes); // No es necesario pasar `db`, Sequelize maneja la conexión

// Inicia el servidor
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en el puerto ${PORT}`);
});
