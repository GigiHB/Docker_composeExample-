# Docker + Python + PostgreSQL Example

This repository is a simple example of how to run a **Python application** connected to a **PostgreSQL database** using **Docker Compose**.  
It’s meant for learning and practicing Docker basics.

---


## 1. Clone the repo
```bash
git clone https://github.com/your-username/docker-postgres-app.git
cd docker-postgres-app
---

## 2. Build and start containers
docker compose up -d
-d run in detached mode to see the logs:
docker compose logs -f

# 3. Found a container while is runing:
docker exec -it docker-postsql-db-1 psql -U postgres -d testdb

## 4.- To stop the container: 
docker compose down

##5.- Delate all volumes:
docker compose down -v
