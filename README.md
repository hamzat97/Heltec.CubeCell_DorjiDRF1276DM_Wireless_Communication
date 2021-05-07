## Heltec.CubeCell_DorjiDRF1276DM_Wireless_Communication
The purpose of this work is to let you know how to adapt with the send and receive functions of LoRa packets which are already developed for Heltec CubeCell development boards (HTCC-AB01, HTCC-AC0X, HTCC-AM01 , HTCC-AB02, HTCC-AB02S, HTCC-AM02, HTCC-AB02A, HTCC-AB03) so that they can communicate with Dorji DRF1276DM modules. Anyway, the communication with the Dorji DRF1276DM LoRa module is not that easy at all, that's why I strongly recommend to visit this [link](https://github.com/taous96/LoRa32u4II_DorjiDRF1276DM_Wireless_Communication) first for more information, because it is relevant in this situation.
### What are Heltec CubeCell Development Boards ?
CubeCell is a new product series made by Heltec team, mainly for LoRa / LoRaWAN node applications. These development boards are based on ASR605x (ASR6501, ASR6502), those chips are already integrated with the PSoC® 4000 series MCU (ARM® Cortex® M0 + Core) and SX1262. The very low power consumption, the compatibility with Arduino IDE and the easy solar panel integration are the best features of these small development boards and are also the main reasons why many people prefer to use them in their applications. For more information about Heltec CubeCell dev-boards, click [here](https://heltec.org/proudct_center/lora/cubecell/).   
### What is Dorji DRF1276DM ?
Dorji DRF1276DM is a type of long-range low data rate data radio modem based on SX1276 from Semtech. It is a low cost transceiver module designed for operations in the unlicensed ISM (Industrial Scientific Medical) and LPRD bands. Frequency spectrum modulation/demodulation, multi-channel operation, high bandwidth efficiency and anti-blocking performance make DRF1276DM modules easy to realize the robust and reliable wireless link. For more information about Dorji DRF1276DM module, click [here](http://www.dorji.com/docs/data/DRF1276DM.pdf).
### What do you need ?
- Heltec CubeCell board (I use Heltec CubeCell HTCC-AB01)
- Dorji DRF1276DM module
- UART-USB converter (to connect Dorji DRF1276DM to your computer via port USB)
- Mini USB cable (to upload the sketch to Heltec CubeCell board)
- Two antennas (868MHz, 915MHz or 433MHz)
- Some FF jumping wires
### What do you have to do ?
#### 1. Install Heltec CubeCell in Arduino IDE
Just visit one of the two links below and you will know how to install Heltec CubeCell boards in Arduino IDE using one of two possible methods.
- [Via Arduino board manager](https://heltec-automation-docs.readthedocs.io/en/latest/cubecell/quick_start.html#use-arduino-board-manager)
- [Via Git](https://heltec-automation-docs.readthedocs.io/en/latest/cubecell/quick_start.html#via-git)
#### 2. Add CubeCell Library in Arduino IDE 
Just copy CubeCell-Arduino-master folder and paste it to your Arduino libraries folder, just like you do always when you want to install an additional Arduino library in Arduino IDE. 
#### 3. Dorji DRF1276DM Setup
Dorji DRF1276DM is a module that needs some configuration before it is ready to be used. To do this, we need to use a DRF tool software (DRF_Tool.exe in DRF Tool folder) and we can only use it on a Windows computer. First, you must connect Dorji DRF1276DM with UART-USB converter using the wiring shown in USB-Adapter_Dorji_Connection image, and then connect the USB interface of the converter with one of the USB ports of your Windows computer. After that, you open DRF_Tool software, you click on "Open", you select the corresponding USB port, then you select the wireless communication parameters as shown in Dorji_DRF1276DM_Configuration image, and you just click on "Write All" once you finish. A success confirmation message should appear below. 
### How do you use this work ?
You can use this work as a base for any project using a wireless communication between the two devices mentioned above. You just need to make some small modifications before you start coding the interesting part of your project right away.

***Some Important Notes:***
- The frequency, the bandwidth and the spreading factor must necessarily be the same for Dorji DRF1276DM module and Heltec CubeCell development board. In my case, I chose the following: 868MHz for the frequency, 7 for the spreding factor (which is 128 chirps in DRF_Tool), 250KHz for the bandwidth. 
- Once you configure Dorji DRF1276DM module using DRF_Tool software on a computer running Windows, you can then use DAC02 USB adapter (images folder) for a better and easier connection without having to make a wired connection. In addition, you can then connect the Dorji module to any device (Computer, Raspberry Pi, etc.), regardless of the operating system used.
- The Arduino sketch and the Python script allows an automatic wireless communication between Dorji DRF1276DM module and Heltec CubeCell dev-board. This last one sends the message "Hello Dorji" every 20 seconds to Dorji DRF1276DM module, and once Dorji DRF1276DM module receives the message "Hello Dorji", it sends automatically "Hello Heltec Cubcell" message to Heltec CubeCell dev-board and so forth.
- The two codes are simple as much as possible and improved by adding comments in order to not make them difficut to read or understand and also to make the changes quickly.

Finally, I remain at your entire disposal, just contact me at my academic mail h.taous@ump.ac.ma if you have any questions or if you need any kind of assistance.
