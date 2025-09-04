######################################################
### Main-Program                                   ###
### Projekt: Merlin                                ###
### Version: 1.01                                  ###
### Datum  : 27.03.2025                            ###
######################################################
from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore


time_on     = 0.2
time_off_1  = 0.4
time_off_2  = 0.2
time_none   = 0.05
time_pause  = 1.5

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
# 0 -> Spiegel -> Ring
# 1 -> Laser Sender
# 2 -> Laser Empfänger

def main():

    print("=== Start Main ===")
    

    MyWS2812.do_all_def()

    try:
        print("Start Main Loop")
 
        while (True):

            # 0 -> Laser 1
            MyWS2812.set_led_obj(6,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 3 -> Laser 2
            MyWS2812.set_led_obj(6,"red2")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 8 -> Boden 1 - 1
            MyWS2812.set_led_obj(0,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(0,"off")
            time.sleep(time_off)
            # 11 -> Boden 1 - 2
            MyWS2812.set_led_obj(0,"red3")
            time.sleep(time_on)
            MyWS2812.set_led_obj(0,"off")
            time.sleep(time_off)
            # 16 -> Spiegel 1
            MyWS2812.set_led_obj(5,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 17 -> Empfänger 1
            MyWS2812.set_led_obj(7,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 19 -> Spiegel 2
            MyWS2812.set_led_obj(5,"red4")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 20 -> Empfänger 2
            MyWS2812.set_led_obj(7,"red")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 32 -> Laser 1
            MyWS2812.set_led_obj(6,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 35 -> Laser 2
            MyWS2812.set_led_obj(6,"red2")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 40 -> Boden 2 - 1
            MyWS2812.set_led_obj(1,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(1,"off")
            time.sleep(time_off)
            # 43 -> Boden 2 - 2
            MyWS2812.set_led_obj(1,"red3")
            time.sleep(time_on)
            MyWS2812.set_led_obj(1,"off")
            time.sleep(time_off)
            # 48 -> Spiegel 1
            MyWS2812.set_led_obj(5,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 49 -> Empfänger 1
            MyWS2812.set_led_obj(7,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 51 -> Spiegel 2
            MyWS2812.set_led_obj(5,"red4")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 52 -> Empfänger 2
            MyWS2812.set_led_obj(7,"red")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 64 -> Laser 1
            MyWS2812.set_led_obj(6,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 67 -> Laser 2
            MyWS2812.set_led_obj(6,"red2")
            time.sleep(time_on)
            MyWS2812.set_led_obj(6,"def")
            time.sleep(time_off)
            # 72 -> Boden 3 - 1
            MyWS2812.set_led_obj(2,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(2,"off")
            time.sleep(time_off)
            # 75 -> Boden 3 - 2
            MyWS2812.set_led_obj(2,"red3")
            time.sleep(time_on)
            MyWS2812.set_led_obj(2,"off")
            time.sleep(time_off)
            # 80 -> Spiegel 1
            MyWS2812.set_led_obj(5,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 81 -> Empfänger 1
            MyWS2812.set_led_obj(7,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 83 -> Spiegel 2
            MyWS2812.set_led_obj(5,"red4")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 84 -> Empfänger 2
            MyWS2812.set_led_obj(7,"red")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 104 -> Boden 4 - 1
            MyWS2812.set_led_obj(3,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(3,"off")
            time.sleep(time_off)
            # 107 -> Boden 4 - 2
            MyWS2812.set_led_obj(3,"red3")
            time.sleep(time_on)
            MyWS2812.set_led_obj(3,"off")
            time.sleep(time_off)
            # 112 -> Spiegel 1
            MyWS2812.set_led_obj(5,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 113 -> Empfänger 1
            MyWS2812.set_led_obj(7,"red1")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            # 115 -> Spiegel 2
            MyWS2812.set_led_obj(5,"red4")
            time.sleep(time_on)
            MyWS2812.set_led_obj(5,"def")
            time.sleep(time_off)
            # 116 -> Empfänger 2
            MyWS2812.set_led_obj(7,"red")
            time.sleep(time_on)
            MyWS2812.set_led_obj(7,"off")
            time.sleep(time_off)
            #----------------------------------------------------------   

            time.sleep(time_pause)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
        MyWS2812.do_all_off()   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_i2c:
        print("I2C_MCP23017 -> Load-Module")
        import libs.module_i2c as MyGPIO
        #print("I2C -> Setup")
        MyGPIO.i2c_setup()
        ### Test ###
        print("I2C -> SetOutput")
        MyGPIO.i2c_write(0,True)
        time.sleep(0.5)
        MyGPIO.i2c_write(0,False)

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___ -> = STOP =")

# ##############################################################################
