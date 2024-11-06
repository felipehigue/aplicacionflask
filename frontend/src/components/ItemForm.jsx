import React, { useState } from 'react';
import { createItem } from '../services/api';

const ItemForm = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        createItem({ name, description }).then(() => {
            setName('');
            setDescription('');
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Nombre"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                type="text"
                placeholder="Descripción"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button type="submit">Crear</button>
        </form>
    );
};

export default ItemForm;
