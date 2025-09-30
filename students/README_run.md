## 1) Crear redes y volumen:
```
docker network create el-lido  
docker network create mojica
docker network create melendez  
docker volume create biblioteca-del-pueblo
```
## 2) Levantar contenedores en las redes:
```
docker run -d --name svc-daniel \
  --network mojica \
  -e STUDENT_NAME="Daniel" \
  -e BARRIO="Mojica" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 your-dockerhub-username/cali-service:v1

  docker run -d --name svc-jonathan \
  --network melendez \
  -e STUDENT_NAME="Jonathan" \
  -e BARRIO="melendez" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 jonmeister/cali-service:v1

  docker run -d --name svc-andrey \
  --network el-lido \
  -e STUDENT_NAME="Andrey" \
  -e BARRIO="El Lido" \
  -v biblioteca-del-pueblo:/var/log/app \
  -p 0:8080 andreyquiceno/cali-service:v1
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