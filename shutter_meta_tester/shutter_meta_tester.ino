
const byte LED_PIN = 3;
const byte BUTTON_PIN = 4;

// pulses duration, in microseconds
//                1/1000   1/2000  1/4000  1/8000
int pulses[] = {   1000,     500,     250,   125};
int pulses_nb = 4;
int pulse_index = 0;
// nb of pulse of each value
int repeat_nb = 3;
int repeat_index = 0;

int previous_duration = -1;

// default is up (1)
byte previous_button_state = 1;


void setup() {

  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.print("Next pulse duration (microseconds) : ");
  Serial.println(pulses[pulse_index]);

}

void loop() {
  // put your main code here, to run repeatedly:
  byte current_button_state = digitalRead(BUTTON_PIN);
  if(current_button_state == LOW && current_button_state != previous_button_state) {
      digitalWrite(LED_PIN, HIGH);
      delayMicroseconds(pulses[pulse_index]);
      digitalWrite(LED_PIN, LOW);

      repeat_index++;
      if(repeat_index >= repeat_nb) {
        repeat_index = 0;
        pulse_index++;
        if(pulse_index >= pulses_nb) {
          pulse_index = 0;
        }
      }
      Serial.print("Next pulse duration (microseconds) : ");
      Serial.println(pulses[pulse_index]);
    
    
  }
  previous_button_state = current_button_state;
  delay(100);


}
