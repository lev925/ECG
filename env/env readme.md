### create
python -m venv env

### activate
Для активации окружение надо запустить скрипт activate.bat внутри директории с виртуальным окружением. Затем выполнить необходимые операции, допустим установить пакет. По окончанию работы запусить скрипт deactivate.bat.


### which python

- import os
- import sys
- os.path.dirname(sys.executable)
