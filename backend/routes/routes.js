const express = require('express');
const router = express.Router();
const camisetaController = require('../controllers/camisetaControllers');

// Ruta para obtener todas las camisetas
router.get('/', camisetaController.getAllCamisetas);

// Ruta para obtener una camiseta por ID
router.get('/:id', camisetaController.getCamisetaById);

// Ruta para crear una nueva camiseta
router.post('/', camisetaController.createCamiseta);

// Ruta para actualizar una camiseta
router.put('/:id', camisetaController.updateCamiseta);

// Ruta para eliminar una camiseta
router.delete('/:id', camisetaController.deleteCamiseta);

module.exports = router;
