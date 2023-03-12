#include "EasyMFRC522.h"

#define MAX_STRING_SIZE 100
#define BLOCK 1

int PIEZO = 9;

EasyMFRC522 rfidReader(10, 5);

void setup() {
  Serial.begin(9600);
  rfidReader.init();
  pinMode(PIEZO, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // put your setup code here, to run once:
  bool success;
  do {
    success = rfidReader.detectTag();
    delay(50);
  } while(!success);

  char stringBuffer[MAX_STRING_SIZE];
  strcpy(stringBuffer, "Test TERI Product");
  int stringSize = strlen(stringBuffer);
  // int result = rfidReader.writeFile(BLOCK, "ProductName", (byte*)stringBuffer, MAX_STRING_SIZE);
  int result = rfidReader.readFile(BLOCK, "ProductName", (byte*)stringBuffer, MAX_STRING_SIZE);
  if(result >= 0) {
    Serial.println("something has been written");
    Serial.print(stringBuffer);
  } else {
    Serial.println("something has not been written");
    tone(PIEZO, 2000);
    delay(500);
    noTone(PIEZO);
    delay(500);
  }

  rfidReader.unselectMifareTag();
  delay(3000);
}
