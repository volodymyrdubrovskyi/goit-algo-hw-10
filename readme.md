# Завдання 2:

Для 100 експериментів (15 000 точок генеруємо), отримали наступні похибки:

| Відносна похибка,%
|-----------------------
|0.089
|0.063
|0.103
|0.067
|0.229
|0.064
|0.227
|0.189
|0.039
|0.234

Середня похибка для 100 експериментів: 0,1304%
 
Наступним кроком я перевірив похибки на серії серій по 150, 200, 250, 300, 350 експериментів.
Середні значення похибок - у таблиці нижче.

| Кількість єкспериментів   | Відносна похибка,%
|100                        |0,130
|150	                    |0,079
|200	                    |0,051
|250	                    |0,056
|300	                    |0,043
|350	                    |0,058

з таблиці видно, що при генерації 15 000 точок в методі Монте-Карло оптимальна кількість експериментів 200. При подальшому зростанні кількості експериментів середня похибка суттєво не зменшується. Для подальшого зменшення похибки слід збільшувати кількість точок в самому методі.