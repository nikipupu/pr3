import serial # импрорт библиотеки pyserial
import time # импрорт библиотеки time
import serial.tools.list_ports # импрорт модуля list_ports библиотеки pyserial
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] # создание списка скоростей
ports = [p.device for p in serial.tools.list_ports.comports()]
port_name = ports[0] # инициализациия переменной port_name с первым элементом в списке ports
port_speed = int(speeds[-1]) # инициализация переменной port_speed с последним элементом в списке speeds
port_timeout = 10 # инициализация переменной port_timeout со значением 10
ard = serial.Serial(port_name, port_speed, timeout = port_timeout)
time.sleep(1) # устанавлиет задержку выполнения кода на x секунд
ard.flushInput() # очищает входной буфер и удаляет все его содержимое
try: # начало блока обработчика исключения
 msg_bin = ard.read(ard.inWaiting()) # cчитывает байты размера из последовательного порта
 msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
 msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
 msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
 msg_str_ = msg_bin.decode() # возвращает байты, декодированные в строку
 print(len(msg_bin)) # вывод в консоль длины строки
except Exception as e: # выполняется при возникновении ошибки
 print('Error!') # вывод в консоль "Error!"
ard.close() # немедленно закрывает порт
time.sleep(1) # устанавливает задержку выполнения кода на x секунд
print(msg_str_) # вывод значения переменной msg_str_
