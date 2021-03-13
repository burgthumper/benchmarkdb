After reboot of machine 
  the container needs restarted via Windows Terminal. Go to project docker folder. Then,
    PS C:\projects\benchmarkdb\docker> docker-compose up -d
  get container id
    PS C:\projects\benchmarkdb\docker> docker ps
  the service needs started, go into
    PS C:\projects\benchmarkdb\docker> docker exec -it 5fa1ee0ab5bb bash
  then start service
    root@5fa1ee0ab5bb:/# service postgresql start
    root@5fa1ee0ab5bb:/# exit
