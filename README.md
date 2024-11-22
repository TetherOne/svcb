1. Долевое строительство
```` 
1. Открытие файла, чтение данных, первый элемент игнорируется
2. Суммирование всех чисел
3. Вычисление процентов, каждая доля делится на общую сумму, для получения процентного соотношения
4. Вывод, округления до трех знаков по запятой
````
````
Сложность по времени: O(n)
Сложность по памяти: O(n)
Ограничения: ~ до 10**6 долей
````
````
Субъективаня сложность: 4/10
Затраченное время: 15 мин
````


2. Мегатрейдер
````
1. Открытие файла, чтение данных
2. Расчитываем стоимость для каждого лота, прибыль с одной облигации и общую прибыль по лоту
3. Сортировка лотов, по критериям: день, прибыль (по убыванию), стоимость (по возрастанию)
4. Покупка лотов, итерируемся по отсортированным лотам и проверяем, может ли трейдер купить лот.
Если может, то покупаем и увеличиваем общую прибыль
5. Вывод прибыли и всех купленных лотов
````
````
Сложность по времени: O(n * logn)
Сложность по памяти: O(n)
Ограничения: ~ до 10**6 лотов
````
````
Субъективаня сложность: 8/10
Затраченное время: 2 ч

Убрал 3-е условие: "Выплаченные купоны по купленным облигациям не реинвестируются,
то есть не увеличивают сумму доступных денежных средств."
````