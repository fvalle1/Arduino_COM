import processing.serial.*;

Serial port;

void setup(){
  //size of window                                                              
  size(254,181);
  //get serial ready                                                            
  println(Serial.list());
  port=new Serial(this,Serial.list()[0],9600);
  port.bufferUntil('\n');
  background(0,0,255);
  PImage arduino, mail;
  //get image from website
  arduino=loadImage("https://www.arduino.cc/new_home/assets/illu-arduino-UNO.png");
  background(arduino);
}

long n=0, nofevents=1;
  String triggername="sun"; //from IFTTT
  Boolean finished=false;

void serialEvent(Serial port){
  //set dark background while calculating
  background(250,250,250);
  String input=port.readStringUntil('\n');
  int values[]=int(split(input,",")); //get a value in array between commas
  String inputs[]=split(input,",");
  //remove white spaces
  if(input!=null) trim(input);
 if(n<nofevents){ 
   //main trigger
 String url="https://maker.ifttt.com/trigger/"+triggername+"/with/key/<IFTTTkey>?value1="+inputs[0]+"&value2="+inputs[1]+"&value3="+inputs[2];
 println(url);
 loadStrings(url);
println("done");
 }else{
   //when done nofevents trigger the classical arduino
  finished=true;
 loadStrings( "https://maker.ifttt.com/trigger/"+"arduino"+"/with/key/<IFTTTkey>?value1="+inputs[0]+"&value2="+"Finito!"+"&value3="+":-)");
 }
   
background(128,210,183);
}

void draw(){
  
}

