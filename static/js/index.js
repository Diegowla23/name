// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  function hist1(){
	message = new Paho.MQTT.Message("historial");
    message.destinationName = "wlady_hp66@hotmail.com/tema2";
    client.send(message);
	  }

  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "wlady_hp66@hotmail.com",
    password: "DiegoWladimir",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
	
    client.subscribe("wlady_hp66@hotmail.com/tema1");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "wlady_hp66@hotmail.com/tema2";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
	mensaje=(message.payloadString);
	console.log(mensaje)
	Ident=(message.payloadString).split(" ")[0];
	datos=(message.payloadString).split(" ")[1];
	fecha=(message.payloadString);

	if (Ident== "S1"){
		document.getElementById("sensor1").innerHTML=datos;
		}
	if (Ident== "S2"){
		document.getElementById("sensor2").innerHTML=datos;
		}
	if (Ident== "H1"){
		document.getElementById("historial1").innerHTML=fecha;
	}
	if (Ident== "H2"){
		document.getElementById("historial2").innerHTML=fecha;
		}
  }
  
