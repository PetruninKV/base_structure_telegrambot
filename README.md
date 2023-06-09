## Базовая структура для создания телеграм бота на Python
Данный проект представляет собой базовую структуру для создания телеграм бота на языке программирования Python с использованием библиотеки aiogram 3.0-beta. Шаблон включает в себя необходимые файлы и директории для разработки. Проект нацелен на упрощение процесса создания телеграм ботов и помощь разработчикам в быстром старте.
Для того, чтобы использовать данную структуру проекта, выполните следующие шаги:

1. Скопируйте структуру проекта с GitHub на свой компьютер:
    - Откройте терминал в папке, где будет храниться ваш будущий проект;
    - Скопируйте проект локально на ваш компьютер, выполнив следующую команду:
        ```bash
        git clone https://github.com/PetruninKV/base_structure_telegrambot.git
        ```
    - Переименуйте папку в соответствии с названием будущего проекта:
        ```bash
        mv base_structure_telegrambot/ [название вашего проекта]
        ```
    - Перейдите в папку проекта и удалите папку .git:
        ```bash
        cd [название вашего проекта]
        rm -rf .git
        ```
        Опция -rf принудительно удалит всю папку рекурсивно (вместе со всем ее содержимым) без запросов подтверждения. Таким образом, вы удалите всю историю коммитов локально, чтобы не "засорять" ею ваш будущий проект, и отвяжете проект от существующего удаленного репозитория.
    - Выполните следующие команды:
        ```bash
        git init
        git add .
        git commit -m "Initial project"
        ```
        Эти команды создадут новый локальный репозиторий Git и первый коммит в рамках вашего проекта.


2. Привяжите ваш локальный репозиторий к удаленному:
    - Создайте удаленный репозиторий и скопируйте ссылку на него.
    - Свяжите ваш локальный репозиторий с вашим новым удаленным репозиторием:
        ```bash
        git remote add origin [ссылка на ваш новый репозиторий]
        ```
    - (Необязательно) Переименуйте основную ветку в любую другую:
        ```bash
        git branch -M [название ветки]
        ```
        По умолчанию, при первом коммите создается ветка master;
    - Отправьте изменения на ваш удаленный репозиторий:
        ```bash
        git push -u origin [название ветки]
        ```
        При первом "push" операции необходимо использовать опцию -u (upstream), которая связывает локальную ветку с удаленной веткой. При последующих push-операциях можно будет вводить только команду git push.


3. Разрабатывайте бота, создавайте коммиты в рамках своего проекта и отправляйте их в удаленный репозиторий:
    - Внесите изменения в проект;
    - Не забудьте изменить файл README, добавив в него описание своего проекта;
    - Добавьте все изменения в индекс:
        ```bash
        git add .
        ```
    - Создайте коммит с описанием ваших изменений:
        ```bash
        git commit -m "Описание ваших изменений"
        ``` 
    - Отправьте изменения на ваш удаленный репозиторий
        ```bash
        git push origin [название ветки]
        ``` 
        Вместо [название ветки] укажите название ветки, в которую необходимо отправить push.
