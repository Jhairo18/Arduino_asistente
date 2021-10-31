String variable;
void setup() {

pinMode(8,OUTPUT);
//Inicialización de la comunicación serial
Serial.begin(9600);
}

void loop() {
  //Este while nos indica que nuestro programa estará a la espera
  //de datos y no saldra de ese bucle hasta que le llegue uno
  while(Serial.available()==0){  
  };
  //Con el comando Serial.readstring() leyemos el dato que nos va a llegar
  //En este caso estará en la espera de un dato que mandará nuestro codigo python
  variable=Serial.readString();

  //Como le llegará un string, lo convertimos a un entero con el metodo .toInt
  if (variable.toInt()==1){
    digitalWrite(8,1);
    }
  else{
    digitalWrite(8,0);
    }
  }
  
