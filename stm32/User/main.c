#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "OLED.h"
#include "Serial.h"
#include "Key.h"
#include "LED.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


uint8_t KeyNum;
uint8_t X_Position = 1;
uint8_t Y_Position = 1;
extern uint8_t Serial_RxFlag;
extern char spaces[16];
extern uint8_t led1;
int main(void)
{
	uint8_t num = 0;
	uint8_t word_num = 0;
	OLED_Init();
	LED_Init();
	Serial_Init();
	
	while (1)
	{
		if (Serial_RxFlag != 0)
		{
			if(led1 == 1)
			{
				LED1_Turn(GPIO_Pin_1);
				LED1_Turn(GPIO_Pin_2);
				LED1_Turn(GPIO_Pin_3);
				LED1_Turn(GPIO_Pin_4);
				LED1_Turn(GPIO_Pin_5);
				led1 = 0;
			}
			word_num++;
			if (Serial_RxFlag == 1)
			{
				Serial_RxFlag = 0;
				if(X_Position <= 15 && Y_Position <= 4 )
				{
					OLED_ShowChinese(Y_Position,X_Position,Serial_RxPacket);
					X_Position = X_Position + 2;
				}
				else if(X_Position <= 15 && Y_Position > 4  )
				{
					Y_Position = 1;
					OLED_ShowChinese(Y_Position,X_Position,Serial_RxPacket);
					X_Position = X_Position + 2;
				}
				else if(X_Position > 15 && Y_Position < 4 )
				{
					Y_Position += 1;
					X_Position = 1;
					OLED_ShowChinese(Y_Position,X_Position,Serial_RxPacket);
					X_Position = X_Position + 2;
				}
				else if(X_Position > 15 && Y_Position >= 4)
				{
					X_Position = 1;
					Y_Position = 1;
					OLED_ShowChinese(Y_Position,X_Position,Serial_RxPacket);
					X_Position = X_Position + 2;
				}
			}
			else
			{


				Serial_RxFlag = 0;
				if(word_num!=8)
				{
					generate_spaces((16 - X_Position + 1),spaces, sizeof(spaces));
					OLED_ShowString(Y_Position,X_Position,spaces);
				}
				word_num = 0;
				Y_Position ++;
				X_Position = 1;
			}
		}
	}
}
