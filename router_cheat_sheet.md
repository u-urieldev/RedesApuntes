<h1>Router</h1>

* Prender un puerto (entra en modo de configuracion intercace)
    <code>interface gigabitEthernet 0/0</code>
    <code>interface fastEthernet 0/0</code>

    * Poner ip a un puerto (despues de prender el puerto)
        <code>ip address **\<ip> \<mascara>** </code>

    * Prender el foco
        <code>no shut</code>


---

* <h3>Configurar DHCP</h3>
    Se necesita estar en modo de configuracion global

    * Crea un conjunto de ips (entra en modo config-dhcp)
        <code> ip dhcp pool **<nombre_red>** </code>

    * Le dice al pool de direcciones cuales son las redes posiles para repartir
        <code> network **\<ip>** **\<mascara>**</code>

    * Establecer el getway para cada cliente
        <code> default-router **<gateway_ip>** </code>

    * Excluir direcciones para que no se repita (o solo una direccion el desde es opcional)
        <code> ip dhcp excluded-address **<ip(desde)>** **<ip(hasta)>** </code>

    