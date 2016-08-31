// Hey Emacs, this is Arduino, but you can consider as if it were -*-c++-*-
//******
//*Schetch for Arduino to talk with a server
//*which possibly call an API
//*circuit is simply a button to pin A0
//*

#define buttonpin A0

void setup(){
Serial.begin(9600);
}

void loop(){
  Serial.println(0);
  //if button is pressed server is activated
  if(digitalRead(buttonpin)) Serial.println(1);
  //improve stability  
delay(1);
}
