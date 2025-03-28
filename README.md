# Homework 5: ⭐️ Development of a basic REST-based application with Token authentication

Author: **Olena Hnyp**

## 📝 Description

This project consists of a REST-based application implemented using FastAPI. It includes three microservices:

- Business service (**business_service.py**) - fetches song lists from Taylor Swift albums using OpenRouter AI.
- Database service (**db_service.py**) - stores and retrieves songs that a user added to a playlist.
- Client service (**client_service.py**) - acts as an intermediary for adding albums, rating songs, and fetching ratings.

The application is containerized using Docker and includes token-based authentication for secure access.

## 🖥 Usage

### How to run the application

1. Clone the repository.
2. Start the application using Docker: **docker-compose up --build**.
3. The services will be available at:
- Business Service: http://localhost:8002
- Database Service: http://localhost:8001
- Client Service: http://localhost:8000

P.S. You can start the applications in your terminal as well. Go to the folder app and run each service separately:
- uvicorn business_service:app --host 0.0.0.0 --port 8002
- uvicorn db_service:app --host 0.0.0.0 --port 8001
- uvicorn client_service:app --host 0.0.0.0 --port 8000

### Results

You can test the application using **test.py**. There are six tests in general. Here you can see their results:

1. The first test checks what happens if a user enters album name. As we can see, it returns a message that the album was added to a playlist. It means that all of the songs that are in the album were added to the database.

![test1](images/test1.png)

2. This test checks what happens if I want to check rating of a song that I haven`t rated yet. It returns a message that this song has not been rated yet.

![test2](images/test2.png)

3. In this test we check if the function that rates songs works correctly. 

![test3](images/test3.png)

As we can see, everything works fine. We just rated a song from the album folklore that is called 'mirrorball'. It was already in a database. However, we can rate songs that are not in the database as well. They will be automatically added to a playlist too.

4. Here we check if we can get a rating of the song we just rated. As we can see, it is possible to get it now.

![test4](images/test4.png)

5. Also, we can retrieve all of the songs we have in our playlist. Here we checked this function. It returned all of the songs from the album folklore we added previously.

![test5](images/test5.png)

6. Also, I tested how it works if a user enter wrong token to authorize. It returns an error.

![test6](images/test6.png)
