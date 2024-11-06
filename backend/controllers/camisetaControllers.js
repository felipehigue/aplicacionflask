const camisetaService = require('../services/camisetaService');

// Controlador para obtener todas las camisetas
async function getAllCamisetas(req, res) {
  try {
    const camisetas = await camisetaService.getAllCamisetas();
    res.json(camisetas);
  } catch (error) {
    res.status(500).json({ message: 'Error al obtener las camisetas', error: error.message });
  }
}

// Controlador para obtener una camiseta por ID
async function getCamisetaById(req, res) {
  try {
    const camiseta = await camisetaService.getCamisetaById(req.params.id);
    if (camiseta) {
      res.json(camiseta);
    } else {
      res.status(404).json({ message: 'Camiseta no encontrada' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error al obtener la camiseta', error: error.message });
  }
}

// Controlador para crear una nueva camiseta
async function createCamiseta(req, res) {
  try {
    const nuevaCamiseta = await camisetaService.createCamiseta(req.body);
    res.status(201).json(nuevaCamiseta);
  } catch (error) {
    res.status(500).json({ message: 'Error al crear la camiseta', error: error.message });
  }
}

// Controlador para actualizar una camiseta
async function updateCamiseta(req, res) {
  try {
    const camisetaActualizada = await camisetaService.updateCamiseta(req.params.id, req.body);
    res.json(camisetaActualizada);
  } catch (error) {
    res.status(500).json({ message: 'Error al actualizar la camiseta', error: error.message });
  }
}

// Controlador para eliminar una camiseta
async function deleteCamiseta(req, res) {
  try {
    await camisetaService.deleteCamiseta(req.params.id);
    res.json({ message: 'Camiseta eliminada con éxito' });
  } catch (error) {
    res.status(500).json({ message: 'Error al eliminar la camiseta', error: error.message });
  }
}

module.exports = {
  getAllCamisetas,
  getCamisetaById,
  createCamiseta,
  updateCamiseta,
  deleteCamiseta
};
