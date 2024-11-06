const Camiseta = require('../models/items');

// Servicio para obtener todas las camisetas
async function getAllCamisetas() {
  return await Camiseta.findAll();
}

// Servicio para obtener una camiseta por ID
async function getCamisetaById(id) {
  return await Camiseta.findByPk(id);
}

// Servicio para crear una nueva camiseta
async function createCamiseta(data) {
  return await Camiseta.create(data);
}

// Servicio para actualizar una camiseta
async function updateCamiseta(id, data) {
  const camiseta = await Camiseta.findByPk(id);
  if (camiseta) {
    return await camiseta.update(data);
  }
  throw new Error('Camiseta no encontrada');
}

// Servicio para eliminar una camiseta
async function deleteCamiseta(id) {
  const camiseta = await Camiseta.findByPk(id);
  if (camiseta) {
    await camiseta.destroy();
    return;
  }
  throw new Error('Camiseta no encontrada');
}

module.exports = {
  getAllCamisetas,
  getCamisetaById,
  createCamiseta,
  updateCamiseta,
  deleteCamiseta
};
