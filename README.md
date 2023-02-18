# DjangoMQ

![python](https://img.shields.io/badge/Python-blue)
![django](https://img.shields.io/badge/Django-green)

**DjangoMQ is a RESTful API that facilitates sending and receiving messages using the RabbitMQ/AMQP protocol.**

## Installation

To install and run the project, you will need `Docker Compose` installed on your system. Once you have Docker Compose installed, you can follow these steps:

#### Clone the project repository:

```bash
git clone https://github.com/SonyaCore/DjangoMQ.git
```

#### Change into the project directory:

```bash
cd DjangoMQ
```

#### Modify config.env with your desired value

#### Build the Docker image:

```bash
docker-compose build
```

#### Start the containers:

```bash
docker-compose up
```

The project will now be running at http://localhost:8080/.

## Usage

The API provides the following endpoints:

- http://localhost:8080/inbox/: Endpoint for receiving messages. The RabbitMQ consumer will save the result to the database.

- http://localhost:8080/send/: Endpoint for sending messages. The message will be produced and saved to the database.

- http://localhost:8080/users/: Endpoint for posting user IDs and messages.

## Environment Variables

The following environment variables can be set in the `config.env` file:

- `MODE`: Set to container if running in a containerized environment, or local if running locally.

---

- `INIT`: Set to true to enable creation of the admin user on startup, or false to skip admin creation.

- `DJANGO_SU_NAME`: The username for the admin user.
- `DJANGO_SU_EMAIL`: The email address for the admin user.
- `DJANGO_SU_PASSWORD`: The password for the admin user.

---

- `DB_ENGINE`: The database engine to use. For now, the project is configured to use SQLite3.
- `DB_USERNAME`: The username for the mysql database.
- `DB_PASS`: The password for the mysql database.
- `DB_HOST`: The hostname for the mysql database.
