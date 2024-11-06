import React, { useEffect, useState } from 'react';
import { getItems, deleteItem } from '../services/api';

const ItemList = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        getItems().then(response => setItems(response.data));
    }, []);

    const handleDelete = (id) => {
        deleteItem(id).then(() => setItems(items.filter(item => item._id !== id)));
    };

    return (
        <div>
            <h1>Items</h1>
            <ul>
                {items.map(item => (
                    <li key={item._id}>
                        {item.talla} - {item.color}- {item.material}- {item.precio}
                        <button onClick={() => handleDelete(item._id)}>Eliminar</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ItemList;
