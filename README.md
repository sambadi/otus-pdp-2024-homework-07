# Седьмое ДЗ в рамках обучения на курсах Otus

HTTP сервер,

## Запуск проекта

Для запуска проекта достаточно:

- склонировать репозиторий;
- установить Python 3.12 любым доступным способом;
- установить [poetry](https://python-poetry.org/docs/#installation)
- установить зависимости выполнив команду

```shell
 poetry install
```

- запуск на выполнение

```shell
  	poetry run python -m homework_07
```

## Запуск нагрузочного тестирования

Достаточно запустить на выполнение команду:

```shell
make run-with-docker
```

В результате будет запущен сервер, который будет принимать HTTP запросы на порту 8080, а так же собранный 
в Docker контейнере Apache HTTP server benchmarking tool (ab) для проведения нагрузочного тестирования.

В результате выполнения теста в консоль выведется информация о результатах тестирования следующего содержания:

```text
Attaching to apache-utils-1
apache-utils-1  | This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
apache-utils-1  | Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
apache-utils-1  | Licensed to The Apache Software Foundation, http://www.apache.org/                                                                                                                                                
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Benchmarking homework (be patient)                                                                                                                                                                                
apache-utils-1  | Completed 100 requests                                                                                                                                                                                            
apache-utils-1  | Completed 200 requests
apache-utils-1  | Completed 300 requests
apache-utils-1  | Completed 400 requests
apache-utils-1  | Completed 500 requests
apache-utils-1  | Completed 600 requests
apache-utils-1  | Completed 700 requests
apache-utils-1  | Completed 800 requests
apache-utils-1  | Completed 900 requests
apache-utils-1  | Completed 1000 requests
apache-utils-1  | Finished 1000 requests
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Server Software:        python                                                                                                                                                                                    
apache-utils-1  | Server Hostname:        homework                                                                                                                                                                                  
apache-utils-1  | Server Port:            8080                                                                                                                                                                                      
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Document Path:          /index.html                                                                                                                                                                               
apache-utils-1  | Document Length:        110 bytes                                                                                                                                                                                 
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Concurrency Level:      10                                                                                                                                                                                        
apache-utils-1  | Time taken for tests:   0.268 seconds                                                                                                                                                                             
apache-utils-1  | Complete requests:      1000                                                                                                                                                                                      
apache-utils-1  | Failed requests:        0                                                                                                                                                                                         
apache-utils-1  | Keep-Alive requests:    0                                                                                                                                                                                         
apache-utils-1  | Total transferred:      191000 bytes                                                                                                                                                                              
apache-utils-1  | HTML transferred:       110000 bytes                                                                                                                                                                              
apache-utils-1  | Requests per second:    3730.54 [#/sec] (mean)                                                                                                                                                                    
apache-utils-1  | Time per request:       2.681 [ms] (mean)                                                                                                                                                                         
apache-utils-1  | Time per request:       0.268 [ms] (mean, across all concurrent requests)
apache-utils-1  | Transfer rate:          695.83 [Kbytes/sec] received                                                                                                                                                              
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Connection Times (ms)                                                                                                                                                                                             
apache-utils-1  |               min  mean[+/-sd] median   max                                                                                                                                                                       
apache-utils-1  | Connect:        0    0   0.0      0       0                                                                                                                                                                       
apache-utils-1  | Processing:     1    2   0.4      2       5                                                                                                                                                                       
apache-utils-1  | Waiting:        1    2   0.4      2       4                                                                                                                                                                       
apache-utils-1  | Total:          1    2   0.4      2       5                                                                                                                                                                       
apache-utils-1  |                                                                                                                                                                                                                   
apache-utils-1  | Percentage of the requests served within a certain time (ms)                                                                                                                                                      
apache-utils-1  |   50%      2
apache-utils-1  |   66%      2                                                                                                                                                                                                      
apache-utils-1  |   75%      2                                                                                                                                                                                                      
apache-utils-1  |   80%      2
apache-utils-1  |   90%      2
apache-utils-1  |   95%      3
apache-utils-1  |   98%      3
apache-utils-1  |   99%      3
apache-utils-1  |  100%      5 (longest request)
apache-utils-1 exited with code 0

```


# Использование Makefile

Для удобства использования в проект добавлена поддержка make actions. Доступны следующий команды:

- `make install` - установка зависимостей;
- `make run` - запуск приложения;
- `make test` - запуск тестов с покрытием;
- `make lint` - запуск проверки кода;
- `make run-with-docker` - запуск приложения и запуск нагрузочного теста с использованием ab из пакета apache-utils.

