import React from 'react';
import ItemList from './components/ItemList';
import ItemForm from './components/ItemForm';

function App() {
    return (
        <div>
            <h1>CRUD de Items</h1>
            <ItemForm />
            <ItemList />
        </div>
    );
}

export default App;

