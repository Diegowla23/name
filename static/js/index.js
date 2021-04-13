//https://www.eclipse.org/paho/clients/js/

function historial() {
	//alert("led on");
	console.log("archivos1");
	//document.getElementById("sensor").innerHTML="led on";
	message = new Paho.MQTT.Message("archivos1");
    	message.destinationName = "wlady_hp66@hotmail.com/tema1";
    	client.send(message);
  
}
function historial2(){	
	//alert("led off");
	console.log("archivos2");
	message = new Paho.MQTT.Message("archivos2");
    	message.destinationName = "wlady_hp66@hotmail.com/tema1";
    	client.send(message);
	//document.getElementById("sensor").innerHTML="led off";
}






// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
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
    message.destinationName = "wlady_hp66@hotmail.com/tema1";
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
        console.log("onMessageArrived:"+message.payloadString);
	 
	archivos=message.payloadString;
	if(archivos[0]=="1"){
	document.getElementById("s1").innerHTML=archivos;
	}
	if(archivos[0]=="2"){
	document.getElementById("s2").innerHTML=archivos;

	}
  }
