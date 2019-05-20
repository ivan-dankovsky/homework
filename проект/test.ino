const int lights_green_red = 2; // красный, зеленый
const int plain_light = 4; // фары
const int beacon = 9; // маячок 
const int pulse = 3; // отсюда приходит импульс

void setup() {
  pinMode(lights_green_red, OUTPUT); 
  pinMode(plain_light, OUTPUT);
  pinMode(beacon, OUTPUT);
  pinMode(pulse, INPUT);
}

void loop() {
  unsigned long pulse_length = pulseIn(pulse, HIGH); // получаем длину импульса
  unsigned long dur1, dur2, dur3, dur4, dur5, dur6, dur7, dur8, dur9, dur10; // варианты длительностей импульса

  if (pulse_length > dur1 and pulse_length < dur2){
    digitalWrite(lights_green_red, LOW);
    digitalWrite(plain_light, LOW);
    digitalWrite(beacon, LOW);
    // все огни выключены
  }
 
  if (pulse_length > dur3 and pulse_length < dur4){
    digitalWrite(lights_green_red, HIGH);
    digitalWrite(plain_light, LOW);
    digitalWrite(beacon, LOW);
    // горят ходовые огни
  } 

  if (pulse_length > dur5 and pulse_length < dur6){
    digitalWrite(lights_green_red, HIGH);
    digitalWrite(plain_light, HIGH);
    digitalWrite(beacon, LOW);
    // горят ходовые и фары
  }
  
  if (pulse_length > dur7 and pulse_length < dur8){
    digitalWrite(lights_green_red, HIGH);
    digitalWrite(plain_light, HIGH);
    digitalWrite(beacon, HIGH);
    delay(500);
    digitalWrite(beacon, LOW);
    delay(500);
    // все включено и мигает маячок
  }
  
  if (pulse_length > dur9 and pulse_length < dur10){
    digitalWrite(plain_light, HIGH);
    
    digitalWrite(lights_green_red, HIGH);
    digitalWrite(beacon, HIGH);
    delay(500);
    digitalWrite(lights_green_red, LOW);
    digitalWrite(beacon, LOW);
    delay(500);
    // все включено, мигают ходовые и маячок
  }
}
