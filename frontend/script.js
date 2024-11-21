const baseURL = "http://localhost:5000"; // URL del backend

document.addEventListener("DOMContentLoaded", () => {
  const formContainer = document.getElementById("form-container");
  const loginForm = document.getElementById("login-form");
  const loginMsg = document.getElementById("login-msg");

  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      const data = {
        usuario: document.getElementById("usuario").value,
        contraseña: document.getElementById("contraseña").value,
      };

      try {
        const response = await fetch(`${baseURL}/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });

        const result = await response.json();

        if (response.ok) {
          // Si el inicio de sesión es exitoso
          window.location.href = "main.html"; // Redirige al menú principal
        } else {
          // Muestra el mensaje de error del servidor
          loginMsg.textContent = result.message || "Error al iniciar sesión";
        }
      } catch (error) {
        loginMsg.textContent = "Error al conectar con el servidor";
      }
    });
  }


  // Botón Crear Usuario
  const crearUsuarioBtn = document.getElementById("crear-usuario-btn");
  if (crearUsuarioBtn) {
    crearUsuarioBtn.addEventListener("click", () => {
      formContainer.innerHTML = `
        <h2>Crear Usuario</h2>
        <form id="crear-usuario-form">
          <label for="id_usuario">ID Usuario:</label>
          <input type="number" id="id_usuario" name="id_usuario" required>
          
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre" required>
          
          <label for="apellido">Apellido:</label>
          <input type="text" id="apellido" name="apellido" required>
          
          <label for="correo">Correo:</label>
          <input type="email" id="correo" name="correo" required>
          
          <label for="rol">Rol:</label>
          <input type="text" id="rol" name="rol" required>
          
          <label for="usuario">Usuario:</label>
          <input type="text" id="usuario" name="usuario" required>
          
          <label for="contraseña">Contraseña:</label>
          <input type="password" id="contraseña" name="contraseña" required>
          
          <button type="submit">Crear</button>
        </form>
        <p id="crear-usuario-msg" class="error"></p>
      `;

      // Manejo del formulario de creación
      const crearUsuarioForm = document.getElementById("crear-usuario-form");
      const crearUsuarioMsg = document.getElementById("crear-usuario-msg");
      crearUsuarioForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const data = {
          id_usuario: document.getElementById("id_usuario").value,
          nombre: document.getElementById("nombre").value,
          apellido: document.getElementById("apellido").value,
          correo: document.getElementById("correo").value,
          rol: document.getElementById("rol").value,
          usuario: document.getElementById("usuario").value,
          contraseña: document.getElementById("contraseña").value,
        };

        try {
          const response = await fetch(`${baseURL}/insertUsuario`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
          });
          const result = await response.json();
          crearUsuarioMsg.textContent = result.message || "Usuario creado con éxito";
        } catch (error) {
          crearUsuarioMsg.textContent = "Error al crear el usuario";
        }
      });
    });
  }

  // Botón Eliminar Usuario
  const eliminarUsuarioBtn = document.getElementById("eliminar-usuario-btn");
  if (eliminarUsuarioBtn) {
    eliminarUsuarioBtn.addEventListener("click", () => {
      formContainer.innerHTML = `
        <h2>Eliminar Usuario</h2>
        <form id="eliminar-usuario-form">
          <label for="id_usuario_eliminar">Digite el ID del usuario a eliminar:</label>
          <input type="number" id="id_usuario_eliminar" name="id_usuario_eliminar" required>
          <button type="submit">Eliminar</button>
        </form>
        <p id="eliminar-usuario-msg" class="error"></p>
      `;

      // Manejo del formulario de eliminación
      const eliminarUsuarioForm = document.getElementById("eliminar-usuario-form");
      const eliminarUsuarioMsg = document.getElementById("eliminar-usuario-msg");
      eliminarUsuarioForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const idUsuario = document.getElementById("id_usuario_eliminar").value;

        try {
          const response = await fetch(`${baseURL}/deleteUsuario/${idUsuario}`, {
            method: "DELETE",
          });
          const result = await response.json();
          eliminarUsuarioMsg.textContent = result.message || "Usuario eliminado con éxito";
        } catch (error) {
          eliminarUsuarioMsg.textContent = "Error al eliminar el usuario";
        }
      });
    });
  }  

  // Manejo del Logout
  const logoutButton = document.getElementById("logout");
  if (logoutButton) {
    logoutButton.addEventListener("click", async () => {
      await fetch(`${baseURL}/logout`, { method: "POST" });
      window.location.href = "index.html";
    });
  }

  document.getElementById("consultar-camiseta-btn").addEventListener("click", () => {
    formContainer.innerHTML = `
      <h2>Consultar Camiseta</h2>
      <form id="consultar-camiseta-form">
        <label for="id_camiseta">ID de la Camiseta:</label>
        <input type="number" id="id_camiseta" name="id_camiseta" required>
        <button type="submit">Consultar</button>
      </form>
      <div id="resultado-camiseta"></div>
    `;
  
    document.getElementById("consultar-camiseta-form").addEventListener("submit", async (event) => {
      event.preventDefault();
      const id = document.getElementById("id_camiseta").value;
  
      try {
        const response = await fetch(`${baseURL}/getCamiseta/${id}`);
        const result = await response.json();
  
        const resultadoDiv = document.getElementById("resultado-camiseta");
        resultadoDiv.innerHTML = ""; // Limpiar el contenedor de resultados anteriores
  
        if (result.statusCode === 404) {
          resultadoDiv.textContent = result.message;
        } else {
          // Crear una lista para mostrar los datos de la camiseta
          const ul = document.createElement("ul");
          for (const key in result) {
            const li = document.createElement("li");
            li.textContent = `${key}: ${result[key]}`;
            ul.appendChild(li);
          }
          resultadoDiv.appendChild(ul);
        }
      } catch (error) {
        document.getElementById("resultado-camiseta").textContent = "Error al consultar la camiseta";
      }
    });
  });
  
  
  // Crear camiseta
  document.getElementById("crear-camiseta-btn").addEventListener("click", () => {
    formContainer.innerHTML = `
      <h2>Crear Camiseta</h2>
      <form id="crear-camiseta-form">
        <label for="id_camiseta">ID:</label>
        <input type="number" id="id_camiseta" name="id_camiseta" required>
        <label for="talla">Talla:</label>
        <input type="text" id="talla" name="talla" required>
        <label for="color">Color:</label>
        <input type="text" id="color" name="color" required>
        <label for="material">Material:</label>
        <input type="text" id="material" name="material" required>
        <label for="precio">Precio:</label>
        <input type="number" step="0.01" id="precio" name="precio" required>
        <button type="submit">Crear</button>
      </form>
      <p id="crear-camiseta-msg"></p>
    `;
  
    document.getElementById("crear-camiseta-form").addEventListener("submit", async (event) => {
      event.preventDefault();
      const data = {
        id_camiseta: document.getElementById("id_camiseta").value,
        talla: document.getElementById("talla").value,
        color: document.getElementById("color").value,
        material: document.getElementById("material").value,
        precio: document.getElementById("precio").value,
      };
  
      try {
        const response = await fetch(`${baseURL}/insertCamiseta`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });
        const result = await response.json();
        document.getElementById("crear-camiseta-msg").textContent = result.message;
      } catch (error) {
        document.getElementById("crear-camiseta-msg").textContent = "Error al crear la camiseta";
      }
    });
    });


    document.getElementById("actualizar-camiseta-btn").addEventListener("click", () => {
        formContainer.innerHTML = `
          <h2>Actualizar Camiseta</h2>
          <form id="buscar-camiseta-form">
            <label for="id_camiseta">ID de la Camiseta:</label>
            <input type="number" id="id_camiseta" name="id_camiseta" required>
            <button type="submit">Buscar</button>
          </form>
          <div id="form-actualizar-camiseta"></div>
        `;
      
        document.getElementById("buscar-camiseta-form").addEventListener("submit", async (event) => {
          event.preventDefault();
          const id = document.getElementById("id_camiseta").value;
      
          try {
            const response = await fetch(`${baseURL}/getCamiseta/${id}`);
            const result = await response.json();
      
            if (result.statusCode === 404) {
              document.getElementById("form-actualizar-camiseta").textContent = result.message;
            } else {
              document.getElementById("form-actualizar-camiseta").innerHTML = `
                <form id="actualizar-camiseta-form">
                  <label for="talla">Talla:</label>
                  <input type="text" id="talla" name="talla" value="${result.talla}" required>
                  <label for="color">Color:</label>
                  <input type="text" id="color" name="color" value="${result.color}" required>
                  <label for="material">Material:</label>
                  <input type="text" id="material" name="material" value="${result.material}" required>
                  <label for="precio">Precio:</label>
                  <input type="number" id="precio" name="precio" value="${result.precio}" step="0.01" required>
                  <button type="submit">Actualizar</button>
                </form>
              `;
      
              document.getElementById("actualizar-camiseta-form").addEventListener("submit", async (event) => {
                event.preventDefault();
      
                const data = {
                  talla: document.getElementById("talla").value,
                  color: document.getElementById("color").value,
                  material: document.getElementById("material").value,
                  precio: parseFloat(document.getElementById("precio").value)
                };
      
                const updateResponse = await fetch(`${baseURL}/updateCamiseta/${id}`, {
                  method: "PUT",
                  headers: { "Content-Type": "application/json" },
                  body: JSON.stringify(data)
                });
      
                const updateResult = await updateResponse.json();
                alert(updateResult.message);
              });
            }
          } catch (error) {
            document.getElementById("form-actualizar-camiseta").textContent = "Error al buscar la camiseta";
          }
        });
      });

    
    document.getElementById("eliminar-camiseta-btn").addEventListener("click", () => {
  formContainer.innerHTML = `
    <h2>Eliminar Camiseta</h2>
    <form id="eliminar-camiseta-form">
      <label for="id_camiseta">ID de la Camiseta:</label>
      <input type="number" id="id_camiseta" name="id_camiseta" required>
      <button type="submit">Eliminar</button>
    </form>
  `;

  document.getElementById("eliminar-camiseta-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const id = document.getElementById("id_camiseta").value;

    try {
      const response = await fetch(`${baseURL}/deleteCamiseta/${id}`, {
        method: "DELETE"
      });

      const result = await response.json();
      alert(result.message);
    } catch (error) {
      alert("Error al eliminar la camiseta");
    }
  });
});
  
});
