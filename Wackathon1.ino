
int piezoPin = 13;
int tiltSensor = 2; 
int button = 8;
int value = 0;
int buttonState=0;

void setup() 
{
  Serial.begin(9600);
  pinMode(piezoPin, OUTPUT);              
  pinMode(tiltSensor, INPUT);                
  pinMode(button, INPUT);
}

void loop() 
{
  buttonState = digitalRead(button);
  Serial.print(buttonState);
  if (buttonState==0){
    Serial.println("Button pressed");
    tone(piezoPin, 7000); 
    delay(1000);        
    noTone(piezoPin);     
    delay(1000);          
  }
  value = digitalRead(tiltSensor);   // reads the value at a digital input 
  //Serial.println(value);
  if (value==1){
    
    tone(piezoPin, 2000); 
    delay(500);        
    noTone(piezoPin);     
    delay(500);          
  }
}
