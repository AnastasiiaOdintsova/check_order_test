# check_order_test
Тест на проверку того, что по треку заказа можно получить данные о заказе (код ответа равен 200) в Яндекс Самокат с помощью API Яндекс Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

SQL-запросы.
Примечание к запросу №1: Хочу обратить внимание, что в приложении присутствует баг, согласно которому, когда курьер принимает заказ, во вкладке «Мои» этот заказ дублируется. Поэтому итоговая таблица отображает в 2 раза больше строк, чем на самом деле было принято заказов.
