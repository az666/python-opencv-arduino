#include<Stepper.h>
#include <Servo.h>
Servo myservo; 
Servo myservo1; 
char serial_line[100] ="";
int serial_line_length=0;
 char val='/';
 #define STEPS 100
 Stepper stepper(STEPS, 8, 9, 10, 11);
 int pos;
 int pos1;
 int i ;
void setup()
{
  Serial.begin(9600);
  pinMode(5,OUTPUT);
  digitalWrite(5,HIGH);
    myservo.attach(3);
      myservo1.attach(4);
   myservo.write(150);  
   myservo1.write(120);  
  stepper.setSpeed(400);
  
}
 void zhixing()
 {                          
    myservo.write(70);//右
    delay(500);
    digitalWrite(5,LOW);//吸
    for (pos = 120;pos>=80;pos-=1)
    {
       myservo1.write(pos);
        delay(15);  
      }
     myservo1.write(120); 
     delay(500);
     myservo.write(150);
  

     /////归位
     delay(1000);
     digitalWrite(5,HIGH); 
                   
  }
void loop()
{
  stepper.step(-1);  
 Serial.println("go");
 val=Serial.read();   
   if (val == 'a')//检测到圆形物体
{

  if (i == 55)
  {
    Serial.println('6');
    zhixing();
  i = 0 ;
    }
    else  i++ ;  //Serial.println(i);
  
  }
  
}
