## 1) Crear redes y volumen:
```
docker network create el-lido  
docker network create mojica
docker network create melendez 
docker network create metropolitano-del-norte
docker network create la-union
docker volume create biblioteca-del-pueblo
```
## 2) Levantar contenedores en las redes:
```
docker run -d --name svc-daniel \
  --network mojica \
  -e STUDENT_NAME="Daniel" \
  -e BARRIO="Mojica" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 danieltrujillo01/cali-service:v1

  docker run -d --name svc-jonathan \
  --network melendez \
  -e STUDENT_NAME="Jonathan" \
  -e BARRIO="Meléndez" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 jonmeister/cali-service:v1

  docker run -d --name svc-francesco \
  --network melendez \
  -e STUDENT_NAME="Francesco" \
  -e BARRIO="Meléndez" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 franktotti/cali-service:v1

  docker run -d --name svc-ivan \
  --network melendez \
  -e STUDENT_NAME="Ivan" \
  -e BARRIO="Meléndez" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 ivanausecha/cali-service:v1

  docker run -d --name svc-andrey \
  --network el-lido \
  -e STUDENT_NAME="Andrey" \
  -e BARRIO="El Lido" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 andreyquiceno/cali-service:v1

docker run -d --name svc-casaviejas \
  --network la-union \
  -e STUDENT_NAME="casaviejas" \
  -e BARRIO="La Union" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 casaviejas842/cali-service:v1

docker run -d --name svc-juanjo \
  --network metropolitano-del-norte \
  -e STUDENT_NAME="Juan José" \
  -e BARRIO="Metropolitano Del Norte" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 kazel2003/cali-service:v1


  ```
## 3) Probar conexión:
```
curl http://localhost:<puerto-contenedor> #mirar con docker ps
```
## 4) Generar tráfico:
```
docker run --rm --network el-lido curlimages/curl -s https://svc-andrey:8080/ # Todos los contenedores van a escuchar por este puerto
```
## 5) Ver últimas 20 líneas del log:
```
docker run --rm -v biblioteca-del-pueblo:/data alpine \                      
  sh -c "tail -n 20 /data/visitas.log" 
```
### Para entrar al volumen:
```
docker run --rm -it -v biblioteca-del-pueblo:/data alpine sh
```
### Para revisar la carpeta data:
```
ls -l /data
```