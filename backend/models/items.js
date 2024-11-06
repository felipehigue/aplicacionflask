const { DataTypes } = require('sequelize');
const sequelize = require('../database');

const Camiseta = sequelize.define('Camiseta', {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },
  talla: {
    type: DataTypes.STRING,
    allowNull: false
  },
  color: {
    type: DataTypes.STRING,
    allowNull: false
  },
  material: {
    type: DataTypes.STRING,
    allowNull: false
  },
  precio: {
    type: DataTypes.FLOAT,
    allowNull: false
  }
}, {
  timestamps: false // Esto desactiva las columnas createdAt y updatedAt
});

module.exports = Camiseta;
