<h1>Switch</h1>

* <h3>General</h3>
    * Ver direccion MAC
        <code>show mac adress-table</code>

    * No me acuerdo que hace
        <code>show start</code>

    * Modo de configuracion general
        <code>config t</code>

--- 

* <h3> Configurar desde terminal  </h3>
    <code>configure terminal</code>

    * cambiar el nombre al switch: poner contraseña para el modo administrador
         <code>hostname **\<name>**</code>

    *  Configurar la consola
        <code>line con 0</code>

        * evitar que te salgan los mensajes
            <code>logging synchronous</code>

        * evitar que pregunte direcciones 
            <code>no ip domain lookup</code>

        * poner contraseña para linea de comandos (siempre cisco)
            <code>password **\<cisco>**</code>

---

* <h3> Memoria </h3>

    * Ver la configuracin acutual
        <code>show run</code>

    * Guardar la configuracion acual en flask
        <code>copy run start</code>

    * Borrar la configuración de la flask
        <code>erase startup-config</code>

    * Arrancar con la configuracion de la flask
        <code>copy run start</code>

